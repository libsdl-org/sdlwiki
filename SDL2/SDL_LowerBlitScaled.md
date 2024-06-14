###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LowerBlitScaled

Perform low-level surface scaled blitting only.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
int SDL_LowerBlitScaled
    (SDL_Surface * src, SDL_Rect * srcrect,
    SDL_Surface * dst, SDL_Rect * dstrect);
```

## Function Parameters

|                              |             |                                                                                    |
| ---------------------------- | ----------- | ---------------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **src**     | the [SDL_Surface](SDL_Surface) structure to be copied from.                        |
| [SDL_Rect](SDL_Rect) *       | **srcrect** | the [SDL_Rect](SDL_Rect) structure representing the rectangle to be copied.        |
| [SDL_Surface](SDL_Surface) * | **dst**     | the [SDL_Surface](SDL_Surface) structure that is the blit target.                  |
| [SDL_Rect](SDL_Rect) *       | **dstrect** | the [SDL_Rect](SDL_Rect) structure representing the rectangle that is copied into. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is a semi-private function and it performs low-level surface blitting,
assuming the input rectangles have already been clipped.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_BlitScaled](SDL_BlitScaled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

