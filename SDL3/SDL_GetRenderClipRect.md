###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderClipRect

Get the clip rectangle for the current target.

## Syntax

```c
int SDL_GetRenderClipRect(SDL_Renderer *renderer, SDL_Rect *rect);

```

## Function Parameters

|                  |                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **renderer**     | the rendering context                                                                                                    |
| **rect**         | an [SDL_Rect](SDL_Rect) structure filled in with the current clipping area or an empty rectangle if clipping is disabled |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_RenderClipEnabled](SDL_RenderClipEnabled)
* [SDL_SetRenderClipRect](SDL_SetRenderClipRect)

----
[CategoryAPI](CategoryAPI)

