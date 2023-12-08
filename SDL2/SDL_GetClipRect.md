###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetClipRect

Get the clipping rectangle for a surface.

## Syntax

```c
void SDL_GetClipRect(SDL_Surface * surface,
                     SDL_Rect * rect);

```

## Function Parameters

|                 |                                                                                         |
| --------------- | --------------------------------------------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface.md) structure representing the surface to be clipped         |
| **rect**        | an [SDL_Rect](SDL_Rect.md) structure filled in with the clipping rectangle for the surface |

## Remarks

When `surface` is the destination of a blit, only the area within the clip
rectangle is drawn into.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_BlitSurface](SDL_BlitSurface.md)
* [SDL_SetClipRect](SDL_SetClipRect.md)

----
[CategoryAPI](CategoryAPI.md)
