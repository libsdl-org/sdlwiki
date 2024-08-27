###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BlitSurface9Grid

Perform a scaled blit using the 9-grid algorithm to a destination surface, which may be of a different format.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_bool SDL_BlitSurface9Grid(SDL_Surface *src, const SDL_Rect *srcrect, int left_width, int right_width, int top_height, int bottom_height, float scale, SDL_ScaleMode scaleMode, SDL_Surface *dst, const SDL_Rect *dstrect);
```

## Function Parameters

|                                |                   |                                                                                                                                      |
| ------------------------------ | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Surface](SDL_Surface) *   | **src**           | the [SDL_Surface](SDL_Surface) structure to be copied from.                                                                          |
| const [SDL_Rect](SDL_Rect) *   | **srcrect**       | the [SDL_Rect](SDL_Rect) structure representing the rectangle to be used for the 9-grid, or NULL to use the entire surface.          |
| int                            | **left_width**    | the width, in pixels, of the left corners in `srcrect`.                                                                              |
| int                            | **right_width**   | the width, in pixels, of the right corners in `srcrect`.                                                                             |
| int                            | **top_height**    | the height, in pixels, of the top corners in `srcrect`.                                                                              |
| int                            | **bottom_height** | the height, in pixels, of the bottom corners in `srcrect`.                                                                           |
| float                          | **scale**         | the scale used to transform the corner of `srcrect` into the corner of `dstrect`, or 0.0f for an unscaled blit.                      |
| [SDL_ScaleMode](SDL_ScaleMode) | **scaleMode**     | scale algorithm to be used.                                                                                                          |
| [SDL_Surface](SDL_Surface) *   | **dst**           | the [SDL_Surface](SDL_Surface) structure that is the blit target.                                                                    |
| const [SDL_Rect](SDL_Rect) *   | **dstrect**       | the [SDL_Rect](SDL_Rect) structure representing the target rectangle in the destination surface, or NULL to fill the entire surface. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

The pixels in the source surface are split into a 3x3 grid, using the
different corner sizes for each corner, and the sides and center making up
the remaining pixels. The corners are then scaled using `scale` and fit
into the corners of the destination rectangle. The sides and center are
then stretched into place to cover the remaining destination rectangle.

## Thread Safety

The same destination surface should not be used from two threads at once.
It is safe to use the same source surface from multiple threads.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_BlitSurface](SDL_BlitSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

