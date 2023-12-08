###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LowerBlitScaled

Perform low-level surface scaled blitting only.

## Syntax

```c
int SDL_LowerBlitScaled
    (SDL_Surface * src, SDL_Rect * srcrect,
    SDL_Surface * dst, SDL_Rect * dstrect);

```

## Function Parameters

|                 |                                                                                   |
| --------------- | --------------------------------------------------------------------------------- |
| **src**         | the [SDL_Surface](SDL_Surface.md) structure to be copied from                        |
| **srcrect**     | the [SDL_Rect](SDL_Rect.md) structure representing the rectangle to be copied        |
| **dst**         | the [SDL_Surface](SDL_Surface.md) structure that is the blit target                  |
| **dstrect**     | the [SDL_Rect](SDL_Rect.md) structure representing the rectangle that is copied into |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This is a semi-private function and it performs low-level surface blitting,
assuming the input rectangles have already been clipped.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_BlitScaled](SDL_BlitScaled.md)

----
[CategoryAPI](CategoryAPI.md)
