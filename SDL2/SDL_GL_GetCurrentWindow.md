###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GL_GetCurrentWindow

Get the currently active OpenGL window.

## Syntax

```c
SDL_Window* SDL_GL_GetCurrentWindow(void);

```

## Return Value

Returns the currently active OpenGL window on success or NULL on failure;
call [SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
