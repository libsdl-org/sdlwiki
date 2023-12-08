###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GL_DeleteContext

Delete an OpenGL context.

## Syntax

```c
int SDL_GL_DeleteContext(SDL_GLContext context);

```

## Function Parameters

|                 |                                  |
| --------------- | -------------------------------- |
| **context**     | the OpenGL context to be deleted |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GL_CreateContext](SDL_GL_CreateContext.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
