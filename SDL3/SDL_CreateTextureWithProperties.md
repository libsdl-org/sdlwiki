###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateTextureWithProperties

Create a texture for a rendering context with the specified properties.

## Syntax

```c
SDL_Texture* SDL_CreateTextureWithProperties(SDL_Renderer *renderer, SDL_PropertiesID props);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | the rendering context |
| **props**        | the properties to use |

## Return Value

Returns a pointer to the created texture or NULL if no rendering context
was active, the format was unsupported, or the width or height were out of
range; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

These are the supported properties:

- [`SDL_PROP_TEXTURE_CREATE_COLORSPACE_NUMBER`](SDL_PROP_TEXTURE_CREATE_COLORSPACE_NUMBER):
  an [SDL_ColorSpace](SDL_ColorSpace) value describing the texture
  colorspace, defaults to [SDL_COLORSPACE_SCRGB](SDL_COLORSPACE_SCRGB) for
  floating point textures, [SDL_COLORSPACE_HDR10](SDL_COLORSPACE_HDR10) for
  10-bit textures, [SDL_COLORSPACE_SRGB](SDL_COLORSPACE_SRGB) for other RGB
  textures and [SDL_COLORSPACE_JPEG](SDL_COLORSPACE_JPEG) for YUV textures.
- [`SDL_PROP_TEXTURE_CREATE_FORMAT_NUMBER`](SDL_PROP_TEXTURE_CREATE_FORMAT_NUMBER):
  one of the enumerated values in
  [SDL_PixelFormatEnum](SDL_PixelFormatEnum), defaults to the best RGBA
  format for the renderer
- [`SDL_PROP_TEXTURE_CREATE_ACCESS_NUMBER`](SDL_PROP_TEXTURE_CREATE_ACCESS_NUMBER):
  one of the enumerated values in [SDL_TextureAccess](SDL_TextureAccess),
  defaults to [SDL_TEXTUREACCESS_STATIC](SDL_TEXTUREACCESS_STATIC)
- [`SDL_PROP_TEXTURE_CREATE_WIDTH_NUMBER`](SDL_PROP_TEXTURE_CREATE_WIDTH_NUMBER):
  the width of the texture in pixels, required
- [`SDL_PROP_TEXTURE_CREATE_HEIGHT_NUMBER`](SDL_PROP_TEXTURE_CREATE_HEIGHT_NUMBER):
  the height of the texture in pixels, required

With the direct3d11 renderer:

- [`SDL_PROP_TEXTURE_CREATE_D3D11_TEXTURE_POINTER`](SDL_PROP_TEXTURE_CREATE_D3D11_TEXTURE_POINTER):
  the ID3D11Texture2D associated with the texture, if you want to wrap an
  existing texture.
- [`SDL_PROP_TEXTURE_CREATE_D3D11_TEXTURE_U_POINTER`](SDL_PROP_TEXTURE_CREATE_D3D11_TEXTURE_U_POINTER):
  the ID3D11Texture2D associated with the U plane of a YUV texture, if you
  want to wrap an existing texture.
- [`SDL_PROP_TEXTURE_CREATE_D3D11_TEXTURE_V_POINTER`](SDL_PROP_TEXTURE_CREATE_D3D11_TEXTURE_V_POINTER):
  the ID3D11Texture2D associated with the V plane of a YUV texture, if you
  want to wrap an existing texture.

With the direct3d12 renderer:

- [`SDL_PROP_TEXTURE_CREATE_D3D12_TEXTURE_POINTER`](SDL_PROP_TEXTURE_CREATE_D3D12_TEXTURE_POINTER):
  the ID3D12Resource associated with the texture, if you want to wrap an
  existing texture.
- [`SDL_PROP_TEXTURE_CREATE_D3D12_TEXTURE_U_POINTER`](SDL_PROP_TEXTURE_CREATE_D3D12_TEXTURE_U_POINTER):
  the ID3D12Resource associated with the U plane of a YUV texture, if you
  want to wrap an existing texture.
- [`SDL_PROP_TEXTURE_CREATE_D3D12_TEXTURE_V_POINTER`](SDL_PROP_TEXTURE_CREATE_D3D12_TEXTURE_V_POINTER):
  the ID3D12Resource associated with the V plane of a YUV texture, if you
  want to wrap an existing texture.

With the metal renderer:

- [`SDL_PROP_TEXTURE_CREATE_METAL_PIXELBUFFER_POINTER`](SDL_PROP_TEXTURE_CREATE_METAL_PIXELBUFFER_POINTER):
  the CVPixelBufferRef associated with the texture, if you want to create a
  texture from an existing pixel buffer.

With the opengl renderer:

- [`SDL_PROP_TEXTURE_CREATE_OPENGL_TEXTURE_NUMBER`](SDL_PROP_TEXTURE_CREATE_OPENGL_TEXTURE_NUMBER):
  the GLuint texture associated with the texture, if you want to wrap an
  existing texture.
- [`SDL_PROP_TEXTURE_CREATE_OPENGL_TEXTURE_UV_NUMBER`](SDL_PROP_TEXTURE_CREATE_OPENGL_TEXTURE_UV_NUMBER):
  the GLuint texture associated with the UV plane of an NV12 texture, if
  you want to wrap an existing texture.
- [`SDL_PROP_TEXTURE_CREATE_OPENGL_TEXTURE_U_NUMBER`](SDL_PROP_TEXTURE_CREATE_OPENGL_TEXTURE_U_NUMBER):
  the GLuint texture associated with the U plane of a YUV texture, if you
  want to wrap an existing texture.
- [`SDL_PROP_TEXTURE_CREATE_OPENGL_TEXTURE_V_NUMBER`](SDL_PROP_TEXTURE_CREATE_OPENGL_TEXTURE_V_NUMBER):
  the GLuint texture associated with the V plane of a YUV texture, if you
  want to wrap an existing texture.

With the opengles2 renderer:

- [`SDL_PROP_TEXTURE_CREATE_OPENGLES2_TEXTURE_NUMBER`](SDL_PROP_TEXTURE_CREATE_OPENGLES2_TEXTURE_NUMBER):
  the GLuint texture associated with the texture, if you want to wrap an
  existing texture.
- [`SDL_PROP_TEXTURE_CREATE_OPENGLES2_TEXTURE_NUMBER`](SDL_PROP_TEXTURE_CREATE_OPENGLES2_TEXTURE_NUMBER):
  the GLuint texture associated with the texture, if you want to wrap an
  existing texture.
- [`SDL_PROP_TEXTURE_CREATE_OPENGLES2_TEXTURE_UV_NUMBER`](SDL_PROP_TEXTURE_CREATE_OPENGLES2_TEXTURE_UV_NUMBER):
  the GLuint texture associated with the UV plane of an NV12 texture, if
  you want to wrap an existing texture.
- [`SDL_PROP_TEXTURE_CREATE_OPENGLES2_TEXTURE_U_NUMBER`](SDL_PROP_TEXTURE_CREATE_OPENGLES2_TEXTURE_U_NUMBER):
  the GLuint texture associated with the U plane of a YUV texture, if you
  want to wrap an existing texture.
- [`SDL_PROP_TEXTURE_CREATE_OPENGLES2_TEXTURE_V_NUMBER`](SDL_PROP_TEXTURE_CREATE_OPENGLES2_TEXTURE_V_NUMBER):
  the GLuint texture associated with the V plane of a YUV texture, if you
  want to wrap an existing texture.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateTextureFromSurface](SDL_CreateTextureFromSurface)
* [SDL_CreateTexture](SDL_CreateTexture)
* [SDL_DestroyTexture](SDL_DestroyTexture)
* [SDL_QueryTexture](SDL_QueryTexture)
* [SDL_UpdateTexture](SDL_UpdateTexture)

----
[CategoryAPI](CategoryAPI)

