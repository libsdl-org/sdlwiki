# SDL_HINT_VIDEO_X11_XRANDR

A variable controlling whether the X11 XRandR extension should be used.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_X11_XRANDR           "SDL_VIDEO_X11_XRANDR"
```

## Remarks

This variable can be set to the following values:

- "0": Disable XRandR
- "1": Enable XRandR

By default SDL will use XRandR.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

