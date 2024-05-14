###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetClipRect

Get the clipping rectangle for a surface.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
void SDL_GetClipRect(SDL_Surface * surface,
                     SDL_Rect * rect);

```

## Function Parameters

|                 |                                                                                         |
| --------------- | --------------------------------------------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) structure representing the surface to be clipped         |
| **rect**        | an [SDL_Rect](SDL_Rect) structure filled in with the clipping rectangle for the surface |

## Remarks

When `surface` is the destination of a blit, only the area within the clip
rectangle is drawn into.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_BlitSurface](SDL_BlitSurface)
- [SDL_SetClipRect](SDL_SetClipRect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

