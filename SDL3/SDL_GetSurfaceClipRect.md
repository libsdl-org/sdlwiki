###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSurfaceClipRect

Get the clipping rectangle for a surface.

## Syntax

```c
int SDL_GetSurfaceClipRect(SDL_Surface *surface, SDL_Rect *rect);

```

## Function Parameters

|                 |                                                                                         |
| --------------- | --------------------------------------------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) structure representing the surface to be clipped         |
| **rect**        | an [SDL_Rect](SDL_Rect) structure filled in with the clipping rectangle for the surface |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

When `surface` is the destination of a blit, only the area within the clip
rectangle is drawn into.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_BlitSurface](SDL_BlitSurface)
* [SDL_SetSurfaceClipRect](SDL_SetSurfaceClipRect)

----
[CategoryAPI](CategoryAPI)

