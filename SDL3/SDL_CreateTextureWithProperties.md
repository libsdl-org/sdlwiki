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
range; call [SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

These are the supported properties:

- "format" (number) - one of the enumerated values in
  [SDL_PixelFormatEnum](SDL_PixelFormatEnum.md), defaults to the best RGBA
  format for the renderer
- "access" (number) - one of the enumerated values in
  [SDL_TextureAccess](SDL_TextureAccess.md), defaults to
  [SDL_TEXTUREACCESS_STATIC](SDL_TEXTUREACCESS_STATIC.md)
- "width" (number) - the width of the texture in pixels, required
- "height" (number) - the height of the texture in pixels, required

With the direct3d11 renderer:

- "d3d11.texture" (pointer) - the ID3D11Texture2D associated with the
  texture, if you want to wrap an existing texture.
- "d3d11.texture_u" (pointer) - the ID3D11Texture2D associated with the U
  plane of a YUV texture, if you want to wrap an existing texture.
- "d3d11.texture_v" (pointer) - the ID3D11Texture2D associated with the V
  plane of a YUV texture, if you want to wrap an existing texture.

With the direct3d12 renderer:

- "d3d12.texture" (pointer) - the ID3D12Resource associated with the
  texture, if you want to wrap an existing texture.
- "d3d12.texture_u" (pointer) - the ID3D12Resource associated with the U
  plane of a YUV texture, if you want to wrap an existing texture.
- "d3d12.texture_v" (pointer) - the ID3D12Resource associated with the V
  plane of a YUV texture, if you want to wrap an existing texture.

With the opengl renderer:

- "opengl.texture" (number) - the GLuint texture associated with the
  texture, if you want to wrap an existing texture.
- "opengl.texture_uv" (number) - the GLuint texture associated with the UV
  plane of an NV12 texture, if you want to wrap an existing texture.
- "opengl.texture_u" (number) - the GLuint texture associated with the U
  plane of a YUV texture, if you want to wrap an existing texture.
- "opengl.texture_v" (number) - the GLuint texture associated with the V
  plane of a YUV texture, if you want to wrap an existing texture.

With the opengles2 renderer:

- "opengles2.texture" (number) - the GLuint texture associated with the
  texture, if you want to wrap an existing texture.
- "opengles2.texture_uv" (number) - the GLuint texture associated with the
  UV plane of an NV12 texture, if you want to wrap an existing texture.
- "opengles2.texture_u" (number) - the GLuint texture associated with the U
  plane of a YUV texture, if you want to wrap an existing texture.
- "opengles2.texture_v" (number) - the GLuint texture associated with the V
  plane of a YUV texture, if you want to wrap an existing texture.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateTextureFromSurface](SDL_CreateTextureFromSurface.md)
* [SDL_CreateTexture](SDL_CreateTexture.md)
* [SDL_DestroyTexture](SDL_DestroyTexture.md)
* [SDL_QueryTexture](SDL_QueryTexture.md)
* [SDL_UpdateTexture](SDL_UpdateTexture.md)

----
[CategoryAPI](CategoryAPI.md)
