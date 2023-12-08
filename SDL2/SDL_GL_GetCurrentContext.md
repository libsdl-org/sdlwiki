###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GL_GetCurrentContext

Get the currently active OpenGL context.

## Syntax

```c
SDL_GLContext SDL_GL_GetCurrentContext(void);

```

## Return Value

Returns the currently active OpenGL context or NULL on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GL_MakeCurrent](SDL_GL_MakeCurrent.md)

----
[CategoryAPI](CategoryAPI.md)
