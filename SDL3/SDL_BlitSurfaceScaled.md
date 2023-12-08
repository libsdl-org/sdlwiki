###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BlitSurfaceScaled

Perform a scaled surface copy to a destination surface.

## Syntax

```c
int SDL_BlitSurfaceScaled
    (SDL_Surface *src, const SDL_Rect *srcrect,
     SDL_Surface *dst, SDL_Rect *dstrect);

```

## Function Parameters

|                 |                                                                                                                                                       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **src**         | the [SDL_Surface](SDL_Surface.md) structure to be copied from                                                                                            |
| **srcrect**     | the [SDL_Rect](SDL_Rect.md) structure representing the rectangle to be copied                                                                            |
| **dst**         | the [SDL_Surface](SDL_Surface.md) structure that is the blit target                                                                                      |
| **dstrect**     | the [SDL_Rect](SDL_Rect.md) structure representing the target rectangle in the destination surface, filled with the actual rectangle used after clipping |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_BlitSurface](SDL_BlitSurface.md)

----
[CategoryAPI](CategoryAPI.md)
