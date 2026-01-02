# SDL_HINT_PS2_GS_MODE

A variable controlling the video mode of the console.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_PS2_GS_MODE    "SDL_PS2_GS_MODE"
```

## Remarks

The variable can be set to the following values:

- "": Console-native. (default)
- "NTSC": 60hz region.
- "PAL": 50hz region.

## Version

This hint is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

