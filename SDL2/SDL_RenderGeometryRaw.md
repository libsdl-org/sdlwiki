###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderGeometryRaw

Render a list of triangles, optionally using a texture and indices into the vertex arrays Color and alpha modulation is done per vertex ([SDL_SetTextureColorMod](SDL_SetTextureColorMod) and [SDL_SetTextureAlphaMod](SDL_SetTextureAlphaMod) are ignored).

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_RenderGeometryRaw(SDL_Renderer *renderer,
                   SDL_Texture *texture,
                   const float *xy, int xy_stride,
                   const SDL_Color *color, int color_stride,
                   const float *uv, int uv_stride,
                   int num_vertices,
                   const void *indices, int num_indices, int size_indices);
```

## Function Parameters

|                                |                  |                                                                                                                       |
| ------------------------------ | ---------------- | --------------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer**     | The rendering context.                                                                                                |
| [SDL_Texture](SDL_Texture) *   | **texture**      | (optional) The SDL texture to use.                                                                                    |
| const float *                  | **xy**           | Vertex positions.                                                                                                     |
| int                            | **xy_stride**    | Byte size to move from one element to the next element.                                                               |
| const [SDL_Color](SDL_Color) * | **color**        | Vertex colors (as [SDL_Color](SDL_Color)).                                                                            |
| int                            | **color_stride** | Byte size to move from one element to the next element.                                                               |
| const float *                  | **uv**           | Vertex normalized texture coordinates.                                                                                |
| int                            | **uv_stride**    | Byte size to move from one element to the next element.                                                               |
| int                            | **num_vertices** | Number of vertices.                                                                                                   |
| const void *                   | **indices**      | (optional) An array of indices into the 'vertices' arrays, if NULL all vertices will be rendered in sequential order. |
| int                            | **num_indices**  | Number of indices.                                                                                                    |
| int                            | **size_indices** | Index size: 1 (byte), 2 (short), 4 (int).                                                                             |

## Return Value

(int) Return 0 on success, or -1 if the operation is not supported.

## Version

This function is available since SDL 2.0.18.

## See Also

- [SDL_RenderGeometry](SDL_RenderGeometry)
- [SDL_Vertex](SDL_Vertex)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

