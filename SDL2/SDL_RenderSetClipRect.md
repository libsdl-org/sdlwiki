###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderSetClipRect

Set the clip rectangle for rendering on the specified target.

## Syntax

```c
int SDL_RenderSetClipRect(SDL_Renderer * renderer,
                          const SDL_Rect * rect);

```

## Function Parameters

|                  |                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------- |
| **renderer**     | the rendering context for which clip rectangle should be set                                                        |
| **rect**         | an [SDL_Rect](SDL_Rect.md) structure representing the clip area, relative to the viewport, or NULL to disable clipping |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_RenderGetClipRect](SDL_RenderGetClipRect.md)
* [SDL_RenderIsClipEnabled](SDL_RenderIsClipEnabled.md)

----
[CategoryAPI](CategoryAPI.md)
