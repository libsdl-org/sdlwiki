###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetRenderViewport

Set the drawing area for rendering on the current target.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
int SDL_SetRenderViewport(SDL_Renderer *renderer, const SDL_Rect *rect);
```

## Function Parameters

|                                |              |                                                                                                                     |
| ------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                                                              |
| const [SDL_Rect](SDL_Rect) *   | **rect**     | the [SDL_Rect](SDL_Rect) structure representing the drawing area, or NULL to set the viewport to the entire target. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
// Example program:
// Using SDL3 to create Render Viewport

#include <SDL3/SDL.h>

int main(int argc, char *argv[])
{
  SDL_Init(SDL_INIT_VIDEO);

  SDL_Window *window = SDL_CreateWindow("RenderViewport Example", 800, 600, 0);
  SDL_Renderer *renderer = SDL_CreateRenderer(window, NULL);

  SDL_Rect VPrect = {100, 100, 100, 100};
  SDL_SetRenderViewport(renderer, &VPrect);

  SDL_SetRenderDrawColorFloat(renderer, 1.0, 0.0, 0.0, 1.0);
  SDL_RenderFillRect(renderer, NULL);

  SDL_SetRenderDrawColorFloat(renderer, 0.0, 1.0, 1.0, 1.0);
  for (int i = 0; i < 8; i++) {
    SDL_FRect rect = {i * 4 , i * 4, 40, 40};
    SDL_RenderRect(renderer, &rect);
  }

  SDL_RenderPresent(renderer);

  SDL_Delay(5000);

  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(window);
  SDL_Quit();
  return 0;
}
```

## See Also

- [SDL_GetRenderViewport](SDL_GetRenderViewport)
- [SDL_RenderViewportSet](SDL_RenderViewportSet)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

