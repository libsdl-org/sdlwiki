###### (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)
# SDL_RenderGeometry

Render a list of triangles, optionally using a texture and indices into the vertex array Color and alpha modulation is done per vertex ([SDL_SetTextureColorMod](SDL_SetTextureColorMod) and [SDL_SetTextureAlphaMod](SDL_SetTextureAlphaMod) are ignored).

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_RenderGeometry(SDL_Renderer *renderer,
                       SDL_Texture *texture,
                       const SDL_Vertex *vertices, int num_vertices,
                       const int *indices, int num_indices);
```

## Function Parameters

|                                  |                  |                                                                                                                              |
| -------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) *   | **renderer**     | The rendering context.                                                                                                       |
| [SDL_Texture](SDL_Texture) *     | **texture**      | (optional) The SDL texture to use.                                                                                           |
| const [SDL_Vertex](SDL_Vertex) * | **vertices**     | Vertices.                                                                                                                    |
| int                              | **num_vertices** | Number of vertices.                                                                                                          |
| const int *                      | **indices**      | (optional) An array of integer indices into the 'vertices' array, if NULL all vertices will be rendered in sequential order. |
| int                              | **num_indices**  | Number of indices.                                                                                                           |

## Return Value

(int) Return 0 on success, or -1 if the operation is not supported.

## Version

This function is available since SDL 2.0.18.

## See Also

- [SDL_RenderGeometryRaw](SDL_RenderGeometryRaw)
- [SDL_Vertex](SDL_Vertex)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

