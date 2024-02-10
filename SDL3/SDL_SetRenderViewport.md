###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetRenderViewport

Set the drawing area for rendering on the current target.

## Syntax

```c
int SDL_SetRenderViewport(SDL_Renderer *renderer, const SDL_Rect *rect);

```

## Function Parameters

|                  |                                                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| **renderer**     | the rendering context                                                                                              |
| **rect**         | the [SDL_Rect](SDL_Rect) structure representing the drawing area, or NULL to set the viewport to the entire target |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetRenderViewport](SDL_GetRenderViewport)
* [SDL_RenderViewportSet](SDL_RenderViewportSet)

----
[CategoryAPI](CategoryAPI)

