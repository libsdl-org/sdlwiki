###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderSetClipRect

Set the clip rectangle for rendering on the specified target.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_RenderSetClipRect(SDL_Renderer * renderer,
                          const SDL_Rect * rect);

```

## Function Parameters

|                  |                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------- |
| **renderer**     | the rendering context for which clip rectangle should be set                                                        |
| **rect**         | an [SDL_Rect](SDL_Rect) structure representing the clip area, relative to the viewport, or NULL to disable clipping |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_RenderGetClipRect](SDL_RenderGetClipRect)
* [SDL_RenderIsClipEnabled](SDL_RenderIsClipEnabled)

----
[CategoryAPI](CategoryAPI)

