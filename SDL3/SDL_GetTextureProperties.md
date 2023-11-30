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

- "SDL.texture.d3d11.texture" (pointer) - the ID3D11Texture2D associated
  with the texture
- "SDL.texture.d3d11.texture_u" (pointer) - the ID3D11Texture2D associated
  with the U plane of a YUV texture
- "SDL.texture.d3d11.texture_v" (pointer) - the ID3D11Texture2D associated
  with the V plane of a YUV texture

With the direct3d12 renderer:

- "SDL.texture.d3d12.texture" (pointer) - the ID3D12Resource associated
  with the texture
- "SDL.texture.d3d12.texture_u" (pointer) - the ID3D12Resource associated
  with the U plane of a YUV texture
- "SDL.texture.d3d12.texture_v" (pointer) - the ID3D12Resource associated
  with the V plane of a YUV texture

With the opengl renderer:

- "SDL.texture.opengl.texture" (number) - the GLuint texture associated
  with the texture
- "SDL.texture.opengl.texture_uv" (number) - the GLuint texture associated
  with the UV plane of an NV12 texture
- "SDL.texture.opengl.texture_u" (number) - the GLuint texture associated
  with the U plane of a YUV texture
- "SDL.texture.opengl.texture_v" (number) - the GLuint texture associated
  with the V plane of a YUV texture
- "SDL.texture.opengl.tex_w" (float) - the texture coordinate width of the
  texture (0.0 - 1.0)
- "SDL.texture.opengl.tex_h" (float) - the texture coordinate height of the
  texture (0.0 - 1.0)

With the opengles2 renderer:

- "SDL.texture.opengles2.texture" (number) - the GLuint texture associated
  with the texture
- "SDL.texture.opengles2.texture_uv" (number) - the GLuint texture
  associated with the UV plane of an NV12 texture
- "SDL.texture.opengles2.texture_u" (number) - the GLuint texture
  associated with the U plane of a YUV texture
- "SDL.texture.opengles2.texture_v" (number) - the GLuint texture
  associated with the V plane of a YUV texture

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetProperty](SDL_GetProperty)
* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI)

