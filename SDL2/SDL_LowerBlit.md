###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LowerBlit

Perform low-level surface blitting only.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
int SDL_LowerBlit
    (SDL_Surface * src, SDL_Rect * srcrect,
     SDL_Surface * dst, SDL_Rect * dstrect);
```

## Function Parameters

|                              |             |                                                                                                                 |
| ---------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **src**     | the [SDL_Surface](SDL_Surface) structure to be copied from.                                                     |
| [SDL_Rect](SDL_Rect) *       | **srcrect** | the [SDL_Rect](SDL_Rect) structure representing the rectangle to be copied, or NULL to copy the entire surface. |
| [SDL_Surface](SDL_Surface) * | **dst**     | the [SDL_Surface](SDL_Surface) structure that is the blit target.                                               |
| [SDL_Rect](SDL_Rect) *       | **dstrect** | the [SDL_Rect](SDL_Rect) structure representing the rectangle that is copied into.                              |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is a semi-private blit function and it performs low-level surface
blitting, assuming the input rectangles have already been clipped.

Unless you know what you're doing, you should be using
[SDL_BlitSurface](SDL_BlitSurface)() instead.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_BlitSurface](SDL_BlitSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

