# SDL_OUT_CAP

Macro that annotates function params with output buffer size.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_OUT_CAP(x) _Out_cap_(x)
```

## Remarks

If we were to annotate `wcsncpy`:

```c
char *wcscpy(SDL_OUT_CAP(bufsize) wchar_t *dst, const wchar_t *src, size_t bufsize);
```

This notes that `dst` should have a capacity of `bufsize` wchar_t in size,
and is only written to by the function. The compiler or other analysis
tools can warn when this doesn't appear to be the case.

This operates on counts of objects, not bytes. Use
[SDL_OUT_BYTECAP](SDL_OUT_BYTECAP) for bytes.

On compilers without this annotation mechanism, this is defined to nothing.

## Version

This macro is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

