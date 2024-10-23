###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_RenderCoordinatesToWindow

Get a point in window coordinates when given a point in render coordinates.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_RenderCoordinatesToWindow(SDL_Renderer *renderer, float x, float y, float *window_x, float *window_y);
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

You may only call this function from the main thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_SetRenderLogicalPresentation](SDL_SetRenderLogicalPresentation)
- [SDL_SetRenderScale](SDL_SetRenderScale)
- [SDL_SetRenderViewport](SDL_SetRenderViewport)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

