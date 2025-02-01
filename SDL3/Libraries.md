# Libraries

These libraries can extend the core SDL functionality.

Please note that several of these have names that start with "SDL_", but none of them are part of the core SDL library. They are _separate_ and _optional_ extras!

## Dear ImGUI:

Dear ImGui is a bloat-free graphical user interface library for C++. It outputs optimized vertex buffers that you can render anytime in your 3D-pipeline-enabled application. It is fast, portable, renderer agnostic, and self-contained (no external dependencies).

- [Dear ImGui website](https://github.com/ocornut/imgui)


## RmlUI:

RmlUi is the C++ user interface package based on the HTML and CSS standards, designed as a complete solution for any project's interface needs. It is a fork of the libRocket project, introducing new features, bug fixes, and performance improvements.

- [RmlUI website](https://github.com/mikke89/RmlUi)
- [Example source code](https://github.com/mikke89/RmlUi/tree/master/Backends)

## SDL_image

Loads images as SDL surfaces and textures, and supports the following formats:
BMP, GIF, JPEG, LBM, PCX, PNG, PNM, SVG, TGA, TIFF, WEBP, XCF, XPM, XV (and more!)

- [Latest Release](https://github.com/libsdl-org/SDL_image/releases/latest)
- [Git Repository](https://github.com/libsdl-org/SDL_image)
- [Wiki](https://wiki.libsdl.org/SDL3_image)

## SDL_mixer

SDL_mixer is a sample multi-channel audio mixer library. It supports any number
of simultaneously playing channels of 16 bit stereo audio, plus a single
channel of music, mixed by the popular FLAC, MikMod MOD, Timidity MIDI, Ogg
Vorbis, and SMPEG MP3 libraries.

SDL_mixer works with SDL3 but we intend to update the API significantly for a 3.0 release.

- [Git Repository](https://github.com/libsdl-org/SDL_mixer)
- [Wiki](https://wiki.libsdl.org/SDL3_mixer)

## SDL_ttf

A library which allows you to use TrueType fonts in your SDL applications. It
comes with an example program "showfont" which displays an example string for a
given TrueType font file.

SDL_ttf works with SDL3 and has a 3.0 [preview release](https://github.com/libsdl-org/SDL_ttf/releases/tag/preview-3.1.0) available.

- [Git Repository](https://github.com/libsdl-org/SDL_ttf)
- [Wiki](https://wiki.libsdl.org/SDL3_ttf)

## SDL_net

A small cross-platform networking library.

SDL_net works with SDL3 and we have some more polish work to do for a 3.0 release.

- [Git Repository](https://github.com/libsdl-org/SDL_net)
- [Wiki](https://wiki.libsdl.org/SDL3_net)

## SDL_shadercross

A library for translating shaders to different formats. Intended for use with the [GPU API](https://wiki.libsdl.org/SDL3/CategoryGPU).

- [Git Repository](https://github.com/libsdl-org/SDL_shadercross)