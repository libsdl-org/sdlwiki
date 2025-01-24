# SDL_RenderCoordinatesFromWindow

Get a point in render coordinates when given a point in window coordinates.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_RenderCoordinatesFromWindow(SDL_Renderer *renderer, float window_x, float window_y, float *x, float *y);
```

## Function Parameters

|                                |              |                                                               |
| ------------------------------ | ------------ | ------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                        |
| float                          | **window_x** | the x coordinate in window coordinates.                       |
| float                          | **window_y** | the y coordinate in window coordinates.                       |
| float *                        | **x**        | a pointer filled with the x coordinate in render coordinates. |
| float *                        | **y**        | a pointer filled with the y coordinate in render coordinates. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This takes into account several states:

- The window dimensions.
- The logical presentation settings
  ([SDL_SetRenderLogicalPresentation](SDL_SetRenderLogicalPresentation))
- The scale ([SDL_SetRenderScale](SDL_SetRenderScale))
- The viewport ([SDL_SetRenderViewport](SDL_SetRenderViewport))

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetRenderLogicalPresentation](SDL_SetRenderLogicalPresentation)
- [SDL_SetRenderScale](SDL_SetRenderScale)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

