# SDL_GL_GetCurrentWindow

Get the currently active OpenGL window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_Window * SDL_GL_GetCurrentWindow(void);
```

## Return Value

([SDL_Window](SDL_Window) *) Returns the currently active OpenGL window on
success or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

