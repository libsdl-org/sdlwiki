# SDL_HINT_VITA_RESOLUTION

A variable overriding the resolution reported on the PlayStation Vita.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VITA_RESOLUTION "SDL_VITA_RESOLUTION"
```

## Remarks

The variable can be set to the following values:

- "544": 544p (default)
- "720": 725p for PSTV
- "1080": 1088i for PSTV

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

