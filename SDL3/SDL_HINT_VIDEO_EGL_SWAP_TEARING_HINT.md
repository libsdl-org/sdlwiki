# SDL_HINT_VIDEO_EGL_SWAP_TEARING_HINT

Let EGL use more specific swapinterval hints.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_EGL_SWAP_TEARING_HINT "SDL_VIDEO_EGL_SWAP_TEARING_HINT"
```

## Remarks

This hint is only used if the video subsystem is using EGL for OpenGL
context management, and the EGL context supports the
EGL_EXT_swap_tearing_hint extension. This lets the app specify the value
for EGL_SWAP_TEARING_HINT_EXT in addition to the normal swap interval
value.

Most apps should not set this hint. SDL will do the normal thing with
standard calls to [SDL_GL_SetSwapInterval](SDL_GL_SetSwapInterval) by
default.

The variable can be set to one of the following values:

- "async": Use EGL_SWAP_TEARING_HINT_ASYNC_EXT.
- "vsync": Use EGL_SWAP_TEARING_HINT_VSYNC_EXT.
- "default": Use EGL_SWAP_TEARING_HINT_DEFAULT_EXT.

This hint should be set before calling
[SDL_GL_SetSwapInterval](SDL_GL_SetSwapInterval).

## Version

This hint is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

