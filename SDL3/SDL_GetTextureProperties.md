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

- [`SDL_PROP_TEXTURE_COLORSPACE_NUMBER`](SDL_PROP_TEXTURE_COLORSPACE_NUMBER):
  an [SDL_ColorSpace](SDL_ColorSpace) value describing the colorspace used
  by the texture
- [`SDL_PROP_TEXTURE_SDR_WHITE_POINT_FLOAT`](SDL_PROP_TEXTURE_SDR_WHITE_POINT_FLOAT):
  for HDR10 and floating point textures, this defines the value of 100%
  diffuse white, with higher values being displayed in the High Dynamic
  Range headroom. This defaults to 100 for HDR10 textures and 1.0 for other
  textures.
- [`SDL_PROP_TEXTURE_HDR_HEADROOM_FLOAT`](SDL_PROP_TEXTURE_HDR_HEADROOM_FLOAT):
  for HDR10 and floating point textures, this defines the maximum dynamic
  range used by the content, in terms of the SDR white point. If this is
  defined, any values outside the range supported by the display will be
  scaled into the available HDR headroom, otherwise they are clipped. This
  defaults to 1.0 for SDR textures, 4.0 for HDR10 textures, and no default
  for floating point textures.

With the direct3d11 renderer:

- [`SDL_PROP_TEXTURE_D3D11_TEXTURE_POINTER`](SDL_PROP_TEXTURE_D3D11_TEXTURE_POINTER):
  the ID3D11Texture2D associated with the texture
- [`SDL_PROP_TEXTURE_D3D11_TEXTURE_U_POINTER`](SDL_PROP_TEXTURE_D3D11_TEXTURE_U_POINTER):
  the ID3D11Texture2D associated with the U plane of a YUV texture
- [`SDL_PROP_TEXTURE_D3D11_TEXTURE_V_POINTER`](SDL_PROP_TEXTURE_D3D11_TEXTURE_V_POINTER):
  the ID3D11Texture2D associated with the V plane of a YUV texture

With the direct3d12 renderer:

- [`SDL_PROP_TEXTURE_D3D12_TEXTURE_POINTER`](SDL_PROP_TEXTURE_D3D12_TEXTURE_POINTER):
  the ID3D12Resource associated with the texture
- [`SDL_PROP_TEXTURE_D3D12_TEXTURE_U_POINTER`](SDL_PROP_TEXTURE_D3D12_TEXTURE_U_POINTER):
  the ID3D12Resource associated with the U plane of a YUV texture
- [`SDL_PROP_TEXTURE_D3D12_TEXTURE_V_POINTER`](SDL_PROP_TEXTURE_D3D12_TEXTURE_V_POINTER):
  the ID3D12Resource associated with the V plane of a YUV texture

With the vulkan renderer:

- [`SDL_PROP_TEXTURE_VULKAN_TEXTURE_POINTER`](SDL_PROP_TEXTURE_VULKAN_TEXTURE_POINTER):
  the VkImage associated with the texture
- [`SDL_PROP_TEXTURE_VULKAN_TEXTURE_U_POINTER`](SDL_PROP_TEXTURE_VULKAN_TEXTURE_U_POINTER):
  the VkImage associated with the U plane of a YUV texture
- [`SDL_PROP_TEXTURE_VULKAN_TEXTURE_V_POINTER`](SDL_PROP_TEXTURE_VULKAN_TEXTURE_V_POINTER):
  the VkImage associated with the V plane of a YUV texture
- [`SDL_PROP_TEXTURE_VULKAN_TEXTURE_UV_POINTER`](SDL_PROP_TEXTURE_VULKAN_TEXTURE_UV_POINTER):
  the VkImage associated with the UV plane of a NV12/NV21 texture

With the opengl renderer:

- [`SDL_PROP_TEXTURE_OPENGL_TEXTURE_NUMBER`](SDL_PROP_TEXTURE_OPENGL_TEXTURE_NUMBER):
  the GLuint texture associated with the texture
- [`SDL_PROP_TEXTURE_OPENGL_TEXTURE_UV_NUMBER`](SDL_PROP_TEXTURE_OPENGL_TEXTURE_UV_NUMBER):
  the GLuint texture associated with the UV plane of an NV12 texture
- [`SDL_PROP_TEXTURE_OPENGL_TEXTURE_U_NUMBER`](SDL_PROP_TEXTURE_OPENGL_TEXTURE_U_NUMBER):
  the GLuint texture associated with the U plane of a YUV texture
- [`SDL_PROP_TEXTURE_OPENGL_TEXTURE_V_NUMBER`](SDL_PROP_TEXTURE_OPENGL_TEXTURE_V_NUMBER):
  the GLuint texture associated with the V plane of a YUV texture
- [`SDL_PROP_TEXTURE_OPENGL_TEXTURE_TARGET_NUMBER`](SDL_PROP_TEXTURE_OPENGL_TEXTURE_TARGET_NUMBER):
  the GLenum for the texture target (`GL_TEXTURE_2D`,
  `GL_TEXTURE_RECTANGLE_ARB`, etc)
- [`SDL_PROP_TEXTURE_OPENGL_TEX_W_FLOAT`](SDL_PROP_TEXTURE_OPENGL_TEX_W_FLOAT):
  the texture coordinate width of the texture (0.0 - 1.0)
- [`SDL_PROP_TEXTURE_OPENGL_TEX_H_FLOAT`](SDL_PROP_TEXTURE_OPENGL_TEX_H_FLOAT):
  the texture coordinate height of the texture (0.0 - 1.0)

With the opengles2 renderer:

- [`SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_NUMBER`](SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_NUMBER):
  the GLuint texture associated with the texture
- [`SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_UV_NUMBER`](SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_UV_NUMBER):
  the GLuint texture associated with the UV plane of an NV12 texture
- [`SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_U_NUMBER`](SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_U_NUMBER):
  the GLuint texture associated with the U plane of a YUV texture
- [`SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_V_NUMBER`](SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_V_NUMBER):
  the GLuint texture associated with the V plane of a YUV texture
- [`SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_TARGET_NUMBER`](SDL_PROP_TEXTURE_OPENGLES2_TEXTURE_TARGET_NUMBER):
  the GLenum for the texture target (`GL_TEXTURE_2D`,
  `GL_TEXTURE_EXTERNAL_OES`, etc)

With the vulkan renderer:

- [`SDL_PROP_TEXTURE_VULKAN_TEXTURE_NUMBER`](SDL_PROP_TEXTURE_VULKAN_TEXTURE_NUMBER):
  the VkImage associated with the texture

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetProperty](SDL_GetProperty)
* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI)

