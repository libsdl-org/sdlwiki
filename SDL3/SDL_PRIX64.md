# SDL_PRIX64

A printf-formatting string for a [Uint64](Uint64) value as upper-case hexadecimal.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_PRIX64 "llX"
```

## Remarks

Use it like this:

```c
SDL_Log("There are %" SDL_PRIX64 " bottles of beer on the wall.", bottles);
```

## Version

This macro is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

