###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderGeometryRawFloat

Render a list of triangles, optionally using a texture and indices into the vertex arrays Color and alpha modulation is done per vertex ([SDL_SetTextureColorMod](SDL_SetTextureColorMod) and [SDL_SetTextureAlphaMod](SDL_SetTextureAlphaMod) are ignored).

## Syntax

```c
int SDL_RenderGeometryRawFloat(SDL_Renderer *renderer,
                       SDL_Texture *texture,
                       const float *xy, int xy_stride,
                       const SDL_FColor *color, int color_stride,
                       const float *uv, int uv_stride,
                       int num_vertices,
                       const void *indices, int num_indices, int size_indices);

```

## Function Parameters

|                      |                                                                                                                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **renderer**         | The rendering context.                                                                                                |
| **texture**          | (optional) The SDL texture to use.                                                                                    |
| **xy**               | Vertex positions                                                                                                      |
| **xy_stride**        | Byte size to move from one element to the next element                                                                |
| **color**            | Vertex colors (as [SDL_FColor](SDL_FColor))                                                                           |
| **color_stride**     | Byte size to move from one element to the next element                                                                |
| **uv**               | Vertex normalized texture coordinates                                                                                 |
| **uv_stride**        | Byte size to move from one element to the next element                                                                |
| **num_vertices**     | Number of vertices.                                                                                                   |
| **indices**          | (optional) An array of indices into the 'vertices' arrays, if NULL all vertices will be rendered in sequential order. |
| **num_indices**      | Number of indices.                                                                                                    |
| **size_indices**     | Index size: 1 (byte), 2 (short), 4 (int)                                                                              |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_RenderGeometry](SDL_RenderGeometry)
* [SDL_Vertex](SDL_Vertex)

----
[CategoryAPI](CategoryAPI)

