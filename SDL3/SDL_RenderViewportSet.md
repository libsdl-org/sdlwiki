###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderViewportSet

Return whether an explicit rectangle was set as the viewport.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_bool SDL_RenderViewportSet(SDL_Renderer *renderer);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | the rendering context |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the viewport was set to a specific
rectangle, or [SDL_FALSE](SDL_FALSE) if it was set to NULL (the entire
target)

## Remarks

This is useful if you're saving and restoring the viewport and want to know
whether you should restore a specific rectangle or NULL. Note that the
viewport is always reset when changing rendering targets.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetRenderViewport](SDL_GetRenderViewport)
* [SDL_SetRenderViewport](SDL_SetRenderViewport)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

