###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetClipRect

Set the clipping rectangle for a surface.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_bool SDL_SetClipRect(SDL_Surface * surface,
                         const SDL_Rect * rect);

```

## Function Parameters

|                 |                                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) structure to be clipped                                              |
| **rect**        | the [SDL_Rect](SDL_Rect) structure representing the clipping rectangle, or NULL to disable clipping |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the rectangle intersects the surface,
otherwise [SDL_FALSE](SDL_FALSE) and blits will be completely clipped.

## Remarks

When `surface` is the destination of a blit, only the area within the clip
rectangle is drawn into.

Note that blits are automatically clipped to the edges of the source and
destination surfaces.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_BlitSurface](SDL_BlitSurface)
* [SDL_GetClipRect](SDL_GetClipRect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

