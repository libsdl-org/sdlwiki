###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetRenderViewport

Set the drawing area for rendering on the current target.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_bool SDL_SetRenderViewport(SDL_Renderer *renderer, const SDL_Rect *rect);
```

## Function Parameters

|                                |              |                                                                                                                     |
| ------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                                                              |
| const [SDL_Rect](SDL_Rect) *   | **rect**     | the [SDL_Rect](SDL_Rect) structure representing the drawing area, or NULL to set the viewport to the entire target. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetRenderViewport](SDL_GetRenderViewport)
- [SDL_RenderViewportSet](SDL_RenderViewportSet)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

