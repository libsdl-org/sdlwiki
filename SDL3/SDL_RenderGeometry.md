###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderGeometry

Render a list of triangles, optionally using a texture and indices into the vertex array Color and alpha modulation is done per vertex ([SDL_SetTextureColorMod](SDL_SetTextureColorMod) and [SDL_SetTextureAlphaMod](SDL_SetTextureAlphaMod) are ignored).

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should use `#include <SDL3/SDL.h>`

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

Returns 0 on success, or -1 if the operation is not supported

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
#include <SDL.h>

int main(int argc, char *argv[]) 
{
  SDL_bool quit = SDL_FALSE;
  SDL_Window *window = SDL_CreateWindow("Triangle Example", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 800, 600, 0);
  SDL_Renderer *renderer = SDL_CreateRenderer(window, NULL, SDL_RENDERER_ACCELERATED);

  SDL_Vertex vert[3];

  // center
  vert[0].position.x = 400;
  vert[0].position.y = 150;
  vert[0].color.r = 255;
  vert[0].color.g = 0;
  vert[0].color.b = 0;
  vert[0].color.a = 255;

  // left
  vert[1].position.x = 200;
  vert[1].position.y = 450;
  vert[1].color.r = 0;
  vert[1].color.g = 0;
  vert[1].color.b = 255;
  vert[1].color.a = 255;

  // right 
  vert[2].position.x = 600;
  vert[2].position.y = 450;
  vert[2].color.r = 0;
  vert[2].color.g = 255;
  vert[2].color.b = 0;
  vert[2].color.a = 255;
 
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

    SDL_RenderGeometry(renderer, NULL, vert, 3, NULL, 0);

    SDL_RenderPresent(renderer);
  }
  
  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(window);
  SDL_Quit();
  return 0;
}
```

## See Also

* [SDL_RenderGeometryRaw](SDL_RenderGeometryRaw)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)


