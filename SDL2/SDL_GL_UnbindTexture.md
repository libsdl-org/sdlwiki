# SDL_GL_UnbindTexture

Unbind an OpenGL/ES/ES2 texture from the current context.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_GL_UnbindTexture(SDL_Texture *texture);
```

## Function Parameters

|                              |             |                                                               |
| ---------------------------- | ----------- | ------------------------------------------------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to unbind from the current OpenGL/ES/ES2 context. |

## Return Value

(int) Returns 0 on success, or -1 if the operation is not supported.

## Remarks

See [SDL_GL_BindTexture](SDL_GL_BindTexture)() for examples on how to use
these functions

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GL_BindTexture](SDL_GL_BindTexture)
- [SDL_GL_MakeCurrent](SDL_GL_MakeCurrent)


## (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

