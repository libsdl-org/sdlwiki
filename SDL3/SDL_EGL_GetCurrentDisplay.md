###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_EGL_GetCurrentDisplay

Get the currently active EGL display.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_EGLDisplay SDL_EGL_GetCurrentDisplay(void);
```

## Return Value

([SDL_EGLDisplay](SDL_EGLDisplay)) Returns the currently active EGL display
or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

