# SDL_HINT_VIDEO_X11_FORCE_EGL

A variable controlling whether X11 should use GLX or EGL by default

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_X11_FORCE_EGL "SDL_VIDEO_X11_FORCE_EGL"
```

## Remarks

This variable can be set to the following values:

- "0": Use GLX
- "1": Use EGL

By default SDL will use GLX when both are present.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

