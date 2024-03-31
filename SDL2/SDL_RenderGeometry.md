###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderGeometry

Render a list of triangles, optionally using a texture and indices into the vertex array Color and alpha modulation is done per vertex ([SDL_SetTextureColorMod](SDL_SetTextureColorMod) and [SDL_SetTextureAlphaMod](SDL_SetTextureAlphaMod) are ignored).

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_RenderGeometry(SDL_Renderer *renderer,
                       SDL_Texture *texture,
                       const SDL_Vertex *vertices, int num_vertices,
                       const int *indices, int num_indices);

```

## Function Parameters

|                      |                                                                                                                              |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **renderer**         | The rendering context.                                                                                                       |
| **texture**          | (optional) The SDL texture to use.                                                                                           |
| **vertices**         | Vertices.                                                                                                                    |
| **num_vertices**     | Number of vertices.                                                                                                          |
| **indices**          | (optional) An array of integer indices into the 'vertices' array, if NULL all vertices will be rendered in sequential order. |
| **num_indices**      | Number of indices.                                                                                                           |

## Return Value

Return 0 on success, or -1 if the operation is not supported

## Version

This function is available since SDL 2.0.18.

## Related Functions

* [SDL_RenderGeometryRaw](SDL_RenderGeometryRaw)
* [SDL_Vertex](SDL_Vertex)


## Example

```c
// Create three vertices to render

SDL_Vertex vertex_1 = {{10.5, 10.5}, {255, 0, 0, 255}, {1, 1}};
SDL_Vertex vertex_2 = {{20.5, 10.5}, {255, 0, 0, 255}, {1, 1}};
SDL_Vertex vertex_3 = {{10.5, 20.5}, {255, 0, 0, 255}, {1, 1}};

// Put them into array

SDL_Vertex vertices[] = {
    vertex_1,
    vertex_2,
    vertex_3
};

// Set renderer color

SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
SDL_RenderClear(renderer);

// Render red triangle

SDL_RenderGeometry(renderer, texture, vertices, 3, NULL, 0);

SDL_RenderPresent(renderer);

```

----
[CategoryAPI](CategoryAPI)

