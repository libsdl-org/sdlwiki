###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LowerBlit

Perform low-level surface blitting only.

## Syntax

```c
int SDL_LowerBlit
    (SDL_Surface * src, SDL_Rect * srcrect,
     SDL_Surface * dst, SDL_Rect * dstrect);

```

## Function Parameters

|                 |                                                                                                                |
| --------------- | -------------------------------------------------------------------------------------------------------------- |
| **src**         | the [SDL_Surface](SDL_Surface.md) structure to be copied from                                                     |
| **srcrect**     | the [SDL_Rect](SDL_Rect.md) structure representing the rectangle to be copied, or NULL to copy the entire surface |
| **dst**         | the [SDL_Surface](SDL_Surface.md) structure that is the blit target                                               |
| **dstrect**     | the [SDL_Rect](SDL_Rect.md) structure representing the rectangle that is copied into                              |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This is a semi-private blit function and it performs low-level surface
blitting, assuming the input rectangles have already been clipped.

Unless you know what you're doing, you should be using
[SDL_BlitSurface](SDL_BlitSurface.md)() instead.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_BlitSurface](SDL_BlitSurface.md)

----
[CategoryAPI](CategoryAPI.md)
