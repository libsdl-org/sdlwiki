# SDL_HINT_WAVE_CHUNK_LIMIT

A variable controlling the maximum number of chunks in a WAVE file.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WAVE_CHUNK_LIMIT "SDL_WAVE_CHUNK_LIMIT"
```

## Remarks

This sets an upper bound on the number of chunks in a WAVE file to avoid
wasting time on malformed or corrupt WAVE files. This defaults to "10000".

This hint should be set before calling [SDL_LoadWAV](SDL_LoadWAV)() or
[SDL_LoadWAV_IO](SDL_LoadWAV_IO)()

## Version

This hint is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

