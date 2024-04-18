#!/usr/bin/env python

from argparse import ArgumentParser
import functools
import multiprocessing
from pathlib import Path
import re
import sys
from typing import Optional
from typing import Union

RE_MARKDOWN_SECTION = re.compile(r"^##\s*([^\n]*)")
RE_MARKDOWN_CODE = re.compile(r"^```([^\n]*)")


def markdown_extract(path: Path):
    results = []
    in_example_section = False
    in_example_block = False
    in_code_block = False
    block_language = None
    language = None
    example_code_lines = []
    for line in path.open().readlines():
        if m := RE_MARKDOWN_SECTION.match(line):
            in_code_block = False
            section = m.groups()[0]
            in_example_section = "example" in section.lower()
            continue
        if in_example_section:
            if m := RE_MARKDOWN_CODE.match(line):
                if not in_code_block:
                    block_language = m.groups()[0]
                    if not block_language:
                        block_language = "c"
                    assert block_language in ("c", "c++", "output"), f"language is \"{block_language}\""
                in_code_block = not in_code_block
                was_in_example_block = in_example_block
                in_example_block = in_code_block and block_language in ("c", "c++")
                if was_in_example_block and not in_example_block:
                    results.append((language, "".join(example_code_lines)))
                    language = None
                    example_code_lines = []
                if in_example_block:
                    language = block_language
                continue
            if in_example_block:
                example_code_lines.append(line)

    return results


RE_MEDIAWIKI_SECTION = re.compile(r"^==([^=]+)==")
RE_MEDIAWIKI_CODE_START = re.compile(r"^\s*<syntaxhighlight lang='([^']+)'\s*>")
RE_MEDIAWIKI_CODE_END = re.compile(r"^\s*</syntaxhighlight>")


def mediawiki_extract(path: Path):
    results = []
    in_example_section = False
    in_code_block = False
    language = None
    example_code_lines = []
    for line in path.open().readlines():
        if m := RE_MEDIAWIKI_SECTION.match(line):
            in_code_block = False
            section = m.groups()[0].strip()
            in_example_section = "code examples" in section.lower()
            continue
        if in_example_section:
            if m := RE_MEDIAWIKI_CODE_START.match(line):
                if not in_code_block:
                    language = m.groups()[0]
                    if not language:
                        language = "c"
                    assert language in ("c", "c++"), f"language is \"{language}\""
                in_code_block = True
                continue
            if in_code_block:
                if m := RE_MEDIAWIKI_CODE_END.match(line):
                    in_code_block = False
                    results.append((language, "".join(example_code_lines)))
                    language = None
                    example_code_lines = []
                    continue
            if in_code_block:
                example_code_lines.append(line)

    return results


def headers_from_path(path: Path) -> list[str]:
    headers = []
    if "SDL2" in path.parts:
        headers.extend(["SDL.h"])
    elif "SDL2_image" in path.parts:
        headers.extend(["SDL_image.h"])
    elif "SDL2_mixer" in path.parts:
        headers.extend(["SDL_mixer.h"])
    elif "SDL2_net" in path.parts:
        headers.extend(["SDL_net.h"])
    elif "SDL2_ttf" in path.parts:
        headers.extend(["SDL_ttf.h"])
    elif "SDL_rtf" in path.parts:
        headers.extend(["SDL_rtf.h"])
    elif "SDL3" in path.parts:
        headers.extend(["SDL3/SDL.h", "SDL3/SDL_opengl.h", "SDL3/SDL_vulkan.h", "vulkan/vulkan.h"])
    elif "SDL3_image" in path.parts:
        headers.extend(["SDL3_image/SDL_image.h"])
    elif "SDL3_mixer" in path.parts:
        headers.extend(["SDL3_mixer/SDL_mixer.h"])
    elif "SDL3_net" in path.parts:
        headers.extend(["SDL3_net/SDL_net.h"])
    elif "SDL3_ttf" in path.parts:
        headers.extend(["SDL3_ttf/SDL_ttf.h"])
    elif "SDL_rtf" in path.parts:
        headers.extend(["SDL_rtf.h"])
    else:
        print("Cannot deduce headers from path", file=sys.stderr)
    return headers


def extract_example(path: Path, docroot: Path, outdir: Path) -> list[Optional[Union[Path, int]]]:
    if path.suffix == ".mediawiki":
        examples = mediawiki_extract(path)
    elif path.suffix == ".md":
        examples = markdown_extract(path)
    else:
        print(f"Invalid document \"{path}\"", file=sys.stderr)
        return 2

    if not examples:
        print(f"No example code found in \"{path}\"", file=sys.stderr)
        return None

    outpaths = []

    for example_i, (language, example_code) in enumerate(examples):
        if "int argc" not in example_code and "#include" not in example_code:
            example_code = "int example_function(void) {\n" + example_code + " return 0;\n}\n"

        if "#include" not in example_code:
            headers = headers_from_path(path)
            if language == "c++":
                headers.extend([
                    "iostream",
                    "vector",
                ])
            headers.extend([
                "stdio.h",
                "stdlib.h",
            ])
            example_code = "\n".join(f"#include <{f}>" for f in headers) + "\n" + example_code

        doc_relative = path.relative_to(docroot)

        out_suffix = {
            "c": ".c",
            "c++": ".cpp",
        }[language]
        outpath = outdir / doc_relative
        if len(examples) > 1:
            outpath = outpath.with_stem(outpath.stem + f"-{example_i + 1}")
        outpath = outpath.with_suffix(out_suffix)

        parent = outpath.parent
        parent.mkdir(exist_ok=True)

        with outpath.open("w") as f:
            f.write(example_code)

        outpaths.append(outpath)
    return outpaths


def main():
    parser = ArgumentParser(allow_abbrev=False)
    parser.add_argument("doc", metavar="DOC", nargs="+", type=Path, help="Documentation sources")
    parser.add_argument("--outdir", required=True, type=Path, help="Output directory")
    parser.add_argument("--docroot", required=True, type=Path, help="Documentation root")
    args = parser.parse_args()

    extract_example_fn = functools.partial(extract_example, docroot=args.docroot, outdir=args.outdir)

    with multiprocessing.Pool(8) as p:
        example_paths = p.map(extract_example_fn, args.doc)

    cmake_example_paths = []
    rc = 0
    for example_path in example_paths:
        if example_path is None:
            continue
        if isinstance(example_path, Path):
            cmake_example_paths.append(str(example_path))
            continue
        if isinstance(example_path, list):
            cmake_example_paths.extend(str(p) for p in example_path)
            continue
        if example_path == 2:
            rc = 2
            continue
        assert False
    print(";".join(cmake_example_paths))
    return rc


if __name__ == "__main__":
    raise SystemExit(main())

