###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_RenderViewportSet

Return whether an explicit rectangle was set as the viewport.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_RenderViewportSet(SDL_Renderer *renderer);
```

## Function Parameters

|                                |              |                        |
| ------------------------------ | ------------ | ---------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context. |

## Return Value

(bool) Returns true if the viewport was set to a specific rectangle, or
false if it was set to NULL (the entire target).

## Remarks

This is useful if you're saving and restoring the viewport and want to know
whether you should restore a specific rectangle or NULL. Note that the
viewport is always reset when changing rendering targets.

## Thread Safety

You may only call this function from the main thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetRenderViewport](SDL_GetRenderViewport)
- [SDL_SetRenderViewport](SDL_SetRenderViewport)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

