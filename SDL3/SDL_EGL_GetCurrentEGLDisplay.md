###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EGL_GetCurrentEGLDisplay

Get the currently active EGL display.

## Syntax

```c
SDL_EGLDisplay SDL_EGL_GetCurrentEGLDisplay(void);

```

## Return Value

Returns the currently active EGL display or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

