###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EGL_GetWindowEGLSurface

Get the EGL surface associated with the window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_EGLSurface SDL_EGL_GetWindowEGLSurface(SDL_Window *window);
```

## Function Parameters

|                            |            |                      |
| -------------------------- | ---------- | -------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to query. |

## Return Value

([SDL_EGLSurface](SDL_EGLSurface)) Returns the EGLSurface pointer
associated with the window, or NULL on failure.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

