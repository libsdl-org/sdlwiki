###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTextureProperties

Get the properties associated with a texture.

## Syntax

```c
SDL_PropertiesID SDL_GetTextureProperties(SDL_Texture *texture);

```

## Function Parameters

|                 |                      |
| --------------- | -------------------- |
| **texture**     | the texture to query |

## Return Value

Returns a valid property ID on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The following read-only properties are provided by SDL:

With the direct3d11 renderer:

- [`SDL_PROPERTY_TEXTURE_D3D11_TEXTURE_POINTER`](SDL_PROPERTY_TEXTURE_D3D11_TEXTURE_POINTER)
  ("SDL.texture.d3d11.texture"): the ID3D11Texture2D associated with the
  texture
- [`SDL_PROPERTY_TEXTURE_D3D11_TEXTURE_U_POINTER`](SDL_PROPERTY_TEXTURE_D3D11_TEXTURE_U_POINTER)
  ("SDL.texture.d3d11.texture_u"): the ID3D11Texture2D associated with the
  U plane of a YUV texture
- [`SDL_PROPERTY_TEXTURE_D3D11_TEXTURE_V_POINTER`](SDL_PROPERTY_TEXTURE_D3D11_TEXTURE_V_POINTER)
  ("SDL.texture.d3d11.texture_v"): the ID3D11Texture2D associated with the
  V plane of a YUV texture

With the direct3d12 renderer:

- [`SDL_PROPERTY_TEXTURE_D3D12_TEXTURE_POINTER`](SDL_PROPERTY_TEXTURE_D3D12_TEXTURE_POINTER)
  ("SDL.texture.d3d12.texture"): the ID3D12Resource associated with the
  texture
- [`SDL_PROPERTY_TEXTURE_D3D12_TEXTURE_U_POINTER`](SDL_PROPERTY_TEXTURE_D3D12_TEXTURE_U_POINTER)
  ("SDL.texture.d3d12.texture_u"): the ID3D12Resource associated with the U
  plane of a YUV texture
- [`SDL_PROPERTY_TEXTURE_D3D12_TEXTURE_V_POINTER`](SDL_PROPERTY_TEXTURE_D3D12_TEXTURE_V_POINTER)
  ("SDL.texture.d3d12.texture_v"): the ID3D12Resource associated with the V
  plane of a YUV texture

With the opengl renderer:

- [`SDL_PROPERTY_TEXTURE_OPENGL_TEXTURE_NUMBER`](SDL_PROPERTY_TEXTURE_OPENGL_TEXTURE_NUMBER)
  ("SDL.texture.opengl.texture"): the GLuint texture associated with the
  texture
- [`SDL_PROPERTY_TEXTURE_OPENGL_TEXTURE_UV_NUMBER`](SDL_PROPERTY_TEXTURE_OPENGL_TEXTURE_UV_NUMBER)
  ("SDL.texture.opengl.texture_uv"): the GLuint texture associated with the
  UV plane of an NV12 texture
- [`SDL_PROPERTY_TEXTURE_OPENGL_TEXTURE_U_NUMBER`](SDL_PROPERTY_TEXTURE_OPENGL_TEXTURE_U_NUMBER)
  ("SDL.texture.opengl.texture_u"): the GLuint texture associated with the
  U plane of a YUV texture
- [`SDL_PROPERTY_TEXTURE_OPENGL_TEXTURE_V_NUMBER`](SDL_PROPERTY_TEXTURE_OPENGL_TEXTURE_V_NUMBER)
  ("SDL.texture.opengl.texture_v"): the GLuint texture associated with the
  V plane of a YUV texture
- [`SDL_PROPERTY_TEXTURE_OPENGL_TEX_W_FLOAT`](SDL_PROPERTY_TEXTURE_OPENGL_TEX_W_FLOAT)
  ("SDL.texture.opengl.tex_w"): the texture coordinate width of the texture
  (0.0 - 1.0)
- [`SDL_PROPERTY_TEXTURE_OPENGL_TEX_H_FLOAT`](SDL_PROPERTY_TEXTURE_OPENGL_TEX_H_FLOAT)
  ("SDL.texture.opengl.tex_h"): the texture coordinate height of the
  texture (0.0 - 1.0)

With the opengles2 renderer:

- [`SDL_PROPERTY_TEXTURE_OPENGLES2_TEXTURE_NUMBER`](SDL_PROPERTY_TEXTURE_OPENGLES2_TEXTURE_NUMBER)
  ("SDL.texture.opengles2.texture"): the GLuint texture associated with the
  texture
- [`SDL_PROPERTY_TEXTURE_OPENGLES2_TEXTURE_UV_NUMBER`](SDL_PROPERTY_TEXTURE_OPENGLES2_TEXTURE_UV_NUMBER)
  ("SDL.texture.opengles2.texture_uv"): the GLuint texture associated with
  the UV plane of an NV12 texture
- [`SDL_PROPERTY_TEXTURE_OPENGLES2_TEXTURE_U_NUMBER`](SDL_PROPERTY_TEXTURE_OPENGLES2_TEXTURE_U_NUMBER)
  ("SDL.texture.opengles2.texture_u"): the GLuint texture associated with
  the U plane of a YUV texture
- [`SDL_PROPERTY_TEXTURE_OPENGLES2_TEXTURE_V_NUMBER`](SDL_PROPERTY_TEXTURE_OPENGLES2_TEXTURE_V_NUMBER)
  ("SDL.texture.opengles2.texture_v"): the GLuint texture associated with
  the V plane of a YUV texture

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetProperty](SDL_GetProperty)
* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI)

