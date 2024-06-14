###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderGeometry

Render a list of triangles, optionally using a texture and indices into the vertex array Color and alpha modulation is done per vertex ([SDL_SetTextureColorMod](SDL_SetTextureColorMod) and [SDL_SetTextureAlphaMod](SDL_SetTextureAlphaMod) are ignored).

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

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
| [SDL_Renderer](SDL_Renderer) *   | **renderer**     | the rendering context.                                                                                                       |
| [SDL_Texture](SDL_Texture) *     | **texture**      | (optional) The SDL texture to use.                                                                                           |
| const [SDL_Vertex](SDL_Vertex) * | **vertices**     | vertices.                                                                                                                    |
| int                              | **num_vertices** | number of vertices.                                                                                                          |
| const int *                      | **indices**      | (optional) An array of integer indices into the 'vertices' array, if NULL all vertices will be rendered in sequential order. |
| int                              | **num_indices**  | number of indices.                                                                                                           |

## Return Value

(int) Returns 0 on success, or -1 if the operation is not supported.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>

int main(int argc, char *argv[])
{
  SDL_bool quit = SDL_FALSE;
  SDL_Window *window = SDL_CreateWindow("Triangle Example", 800, 600, 0);

  SDL_Renderer *renderer = SDL_CreateRenderer(window, NULL);

  #define vertLen 3
  SDL_Vertex vert[vertLen];

  // center
  vert[0].position.x = 400;
  vert[0].position.y = 150;
  vert[0].color.r = 1.0;
  vert[0].color.g = 0.0;
  vert[0].color.b = 0.0;
  vert[0].color.a = 1.0;

  // left
  vert[1].position.x = 200;
  vert[1].position.y = 450;
  vert[1].color.r = 0.0;
  vert[1].color.g = 0.0;
  vert[1].color.b = 1.0;
  vert[1].color.a = 1.0;

  // right
  vert[2].position.x = 600;
  vert[2].position.y = 450;
  vert[2].color.r = 0.0;
  vert[2].color.g = 1.0;
  vert[2].color.b = 0.0;
  vert[2].color.a = 1.0;

  while (!quit) {
   SDL_Event ev;
   while (SDL_PollEvent(&ev) != 0) {
      switch(ev.type) {
        case SDL_EVENT_QUIT:
        quit = SDL_TRUE;
        break;
      }
    }
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderClear(renderer);

    SDL_RenderGeometry(renderer, NULL, vert, vertLen, NULL, 0);

    SDL_RenderPresent(renderer);
  }

  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(window);
  SDL_Quit();
  return 0;
}

```

## See Also

- [SDL_RenderGeometryRaw](SDL_RenderGeometryRaw)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

