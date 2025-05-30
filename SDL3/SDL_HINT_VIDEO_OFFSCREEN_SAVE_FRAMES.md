# SDL_HINT_VIDEO_OFFSCREEN_SAVE_FRAMES

A variable controlling whether the offscreen video driver saves output frames.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_OFFSCREEN_SAVE_FRAMES "SDL_VIDEO_OFFSCREEN_SAVE_FRAMES"
```

## Remarks

This only saves frames that are generated using software rendering, not
accelerated OpenGL rendering.

- "0": Video frames are not saved to disk. (default)
- "1": Video frames are saved to files in the format
  "[SDL_windowX](SDL_windowX)-Y.bmp", where X is the window ID, and Y is
  the frame number.

This hint can be set anytime.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

