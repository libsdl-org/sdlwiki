###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetSurfaceClipRect

Set the clipping rectangle for a surface.

## Syntax

```c
SDL_bool SDL_SetSurfaceClipRect(SDL_Surface *surface,
                         const SDL_Rect *rect);

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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_BlitSurface](SDL_BlitSurface)
* [SDL_GetSurfaceClipRect](SDL_GetSurfaceClipRect)

----
[CategoryAPI](CategoryAPI)

