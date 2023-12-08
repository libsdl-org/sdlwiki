###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderGetClipRect

Get the clip rectangle for the current target.

## Syntax

```c
void SDL_RenderGetClipRect(SDL_Renderer * renderer,
                           SDL_Rect * rect);

```

## Function Parameters

|                  |                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **renderer**     | the rendering context from which clip rectangle should be queried                                                        |
| **rect**         | an [SDL_Rect](SDL_Rect.md) structure filled in with the current clipping area or an empty rectangle if clipping is disabled |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_RenderIsClipEnabled](SDL_RenderIsClipEnabled.md)
* [SDL_RenderSetClipRect](SDL_RenderSetClipRect.md)

----
[CategoryAPI](CategoryAPI.md)
