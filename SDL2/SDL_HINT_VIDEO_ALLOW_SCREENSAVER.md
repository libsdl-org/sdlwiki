###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_VIDEO_ALLOW_SCREENSAVER

A variable controlling whether the screensaver is enabled.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_ALLOW_SCREENSAVER    "SDL_VIDEO_ALLOW_SCREENSAVER"
```

## Remarks

This variable can be set to the following values:

- "0": Disable screensaver
- "1": Enable screensaver

By default SDL will disable the screensaver.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints), [CategoryAPIMacro](CategoryAPIMacro), 

