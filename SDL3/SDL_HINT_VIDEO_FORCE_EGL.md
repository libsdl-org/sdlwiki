# SDL_HINT_VIDEO_FORCE_EGL

A variable controlling whether the OpenGL context should be created with EGL.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_FORCE_EGL "SDL_VIDEO_FORCE_EGL"
```

## Remarks

The variable can be set to the following values:

- "0": Use platform-specific GL context creation API (GLX, WGL, CGL, etc).
  (default)
- "1": Use EGL

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

