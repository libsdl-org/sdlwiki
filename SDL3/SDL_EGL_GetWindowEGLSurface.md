###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EGL_GetWindowEGLSurface

Get the EGL surface associated with the window.

## Syntax

```c
SDL_EGLSurface SDL_EGL_GetWindowEGLSurface(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns the EGLSurface pointer associated with the window, or NULL on
failure.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

