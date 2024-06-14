###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderCoordinatesToWindow

Get a point in window coordinates when given a point in render coordinates.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
int SDL_RenderCoordinatesToWindow(SDL_Renderer *renderer, float x, float y, float *window_x, float *window_y);
```

## Function Parameters

|                                |              |                                                               |
| ------------------------------ | ------------ | ------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                        |
| float                          | **x**        | the x coordinate in render coordinates.                       |
| float                          | **y**        | the y coordinate in render coordinates.                       |
| float *                        | **window_x** | a pointer filled with the x coordinate in window coordinates. |
| float *                        | **window_y** | a pointer filled with the y coordinate in window coordinates. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetRenderLogicalPresentation](SDL_SetRenderLogicalPresentation)
- [SDL_SetRenderScale](SDL_SetRenderScale)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

