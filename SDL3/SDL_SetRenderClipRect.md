###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetRenderClipRect

Set the clip rectangle for rendering on the specified target.

## Syntax

```c
int SDL_SetRenderClipRect(SDL_Renderer *renderer, const SDL_Rect *rect);

```

## Function Parameters

|                  |                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------- |
| **renderer**     | the rendering context                                                                                               |
| **rect**         | an [SDL_Rect](SDL_Rect) structure representing the clip area, relative to the viewport, or NULL to disable clipping |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetRenderClipRect](SDL_GetRenderClipRect)
* [SDL_RenderClipEnabled](SDL_RenderClipEnabled)

----
[CategoryAPI](CategoryAPI)

