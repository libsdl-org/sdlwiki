###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GL_UnbindTexture

Unbind an OpenGL/ES/ES2 texture from the current context.

## Syntax

```c
int SDL_GL_UnbindTexture(SDL_Texture *texture);

```

## Function Parameters

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| **texture**     | the texture to unbind from the current OpenGL/ES/ES2 context |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

See [SDL_GL_BindTexture](SDL_GL_BindTexture.md)() for examples on how to use
these functions

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GL_BindTexture](SDL_GL_BindTexture.md)
* [SDL_GL_MakeCurrent](SDL_GL_MakeCurrent.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryRender](CategoryRender.md)
