###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GL_BindTexture

Bind an OpenGL/ES/ES2 texture to the current context.

## Syntax

```c
int SDL_GL_BindTexture(SDL_Texture *texture, float *texw, float *texh);

```

## Function Parameters

|                 |                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------ |
| **texture**     | the texture to bind to the current OpenGL/ES/ES2 context                                                     |
| **texw**        | a pointer to a float value which will be filled with the texture width or NULL if you don't need that value  |
| **texh**        | a pointer to a float value which will be filled with the texture height or NULL if you don't need that value |

## Return Value

Returns 0 on success, or -1 if the operation is not supported; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This is for use with OpenGL instructions when rendering OpenGL primitives
directly.

If not NULL, `texw` and `texh` will be filled with the width and height
values suitable for the provided texture. In most cases, both will be 1.0,
however, on systems that support the GL_ARB_texture_rectangle extension,
these values will actually be the pixel width and height used to create the
texture, so this factor needs to be taken into account when providing
texture coordinates to OpenGL.

You need a renderer to create an [SDL_Texture](SDL_Texture.md), therefore you
can only use this function with an implicit OpenGL context from
[SDL_CreateRenderer](SDL_CreateRenderer.md)(), not with your own OpenGL
context. If you need control over your OpenGL context, you need to write
your own texture-loading methods.

Also note that SDL may upload RGB textures as BGR (or vice-versa), and
re-order the color channels in the shaders phase, so the uploaded texture
may have swapped color channels.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GL_MakeCurrent](SDL_GL_MakeCurrent.md)
* [SDL_GL_UnbindTexture](SDL_GL_UnbindTexture.md)

----
[CategoryAPI](CategoryAPI.md)
