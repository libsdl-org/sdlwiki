###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
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

Returns 0 on success, or -1 if the operation is not supported

## Remarks

See [SDL_GL_BindTexture](SDL_GL_BindTexture.md)() for examples on how to use
these functions

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GL_BindTexture](SDL_GL_BindTexture.md)
* [SDL_GL_MakeCurrent](SDL_GL_MakeCurrent.md)

----
[CategoryAPI](CategoryAPI.md)
