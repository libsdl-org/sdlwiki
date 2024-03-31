###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderCoordinatesToWindow

Get a point in window coordinates when given a point in render coordinates.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_RenderCoordinatesToWindow(SDL_Renderer *renderer, float x, float y, float *window_x, float *window_y);

```

## Function Parameters

|                  |                                                              |
| ---------------- | ------------------------------------------------------------ |
| **renderer**     | the rendering context                                        |
| **x**            | the x coordinate in render coordinates                       |
| **y**            | the y coordinate in render coordinates                       |
| **window_x**     | a pointer filled with the x coordinate in window coordinates |
| **window_y**     | a pointer filled with the y coordinate in window coordinates |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetRenderLogicalPresentation](SDL_SetRenderLogicalPresentation)
* [SDL_SetRenderScale](SDL_SetRenderScale)

----
[CategoryAPI](CategoryAPI)

