# SDL_BlitSurfaceTiledWithScale

Perform a scaled and tiled blit to a destination surface, which may be of a different format.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_BlitSurfaceTiledWithScale(SDL_Surface *src, const SDL_Rect *srcrect, float scale, SDL_ScaleMode scaleMode, SDL_Surface *dst, const SDL_Rect *dstrect);
```

## Function Parameters

|                                |               |                                                                                                                                      |
| ------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Surface](SDL_Surface) *   | **src**       | the [SDL_Surface](SDL_Surface) structure to be copied from.                                                                          |
| const [SDL_Rect](SDL_Rect) *   | **srcrect**   | the [SDL_Rect](SDL_Rect) structure representing the rectangle to be copied, or NULL to copy the entire surface.                      |
| float                          | **scale**     | the scale used to transform srcrect into the destination rectangle, e.g. a 32x32 texture with a scale of 2 would fill 64x64 tiles.   |
| [SDL_ScaleMode](SDL_ScaleMode) | **scaleMode** | scale algorithm to be used.                                                                                                          |
| [SDL_Surface](SDL_Surface) *   | **dst**       | the [SDL_Surface](SDL_Surface) structure that is the blit target.                                                                    |
| const [SDL_Rect](SDL_Rect) *   | **dstrect**   | the [SDL_Rect](SDL_Rect) structure representing the target rectangle in the destination surface, or NULL to fill the entire surface. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The pixels in `srcrect` will be scaled and repeated as many times as needed
to completely fill `dstrect`.

## Thread Safety

Only one thread should be using the `src` and `dst` surfaces at any given
time.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_BlitSurface](SDL_BlitSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

