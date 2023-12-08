###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetClipRect

Set the clipping rectangle for a surface.

## Syntax

```c
SDL_bool SDL_SetClipRect(SDL_Surface * surface,
                         const SDL_Rect * rect);

```

## Function Parameters

|                 |                                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface.md) structure to be clipped                                              |
| **rect**        | the [SDL_Rect](SDL_Rect.md) structure representing the clipping rectangle, or NULL to disable clipping |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the rectangle intersects the surface,
otherwise [SDL_FALSE](SDL_FALSE.md) and blits will be completely clipped.

## Remarks

When `surface` is the destination of a blit, only the area within the clip
rectangle is drawn into.

Note that blits are automatically clipped to the edges of the source and
destination surfaces.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_BlitSurface](SDL_BlitSurface.md)
* [SDL_GetClipRect](SDL_GetClipRect.md)

----
[CategoryAPI](CategoryAPI.md)
