###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BlitSurfaceUncheckedScaled

Perform low-level surface scaled blitting only.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
int SDL_BlitSurfaceUncheckedScaled(SDL_Surface *src, const SDL_Rect *srcrect, SDL_Surface *dst, const SDL_Rect *dstrect, SDL_ScaleMode scaleMode);
```

## Function Parameters

|                                |               |                                                                                                 |
| ------------------------------ | ------------- | ----------------------------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) *   | **src**       | the [SDL_Surface](SDL_Surface) structure to be copied from                                      |
| const [SDL_Rect](SDL_Rect) *   | **srcrect**   | the [SDL_Rect](SDL_Rect) structure representing the rectangle to be copied                      |
| [SDL_Surface](SDL_Surface) *   | **dst**       | the [SDL_Surface](SDL_Surface) structure that is the blit target                                |
| const [SDL_Rect](SDL_Rect) *   | **dstrect**   | the [SDL_Rect](SDL_Rect) structure representing the target rectangle in the destination surface |
| [SDL_ScaleMode](SDL_ScaleMode) | **scaleMode** | scale algorithm to be used                                                                      |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is a semi-private function and it performs low-level surface blitting,
assuming the input rectangles have already been clipped.

## Thread Safety

The same destination surface should not be used from two threads at once.
It is safe to use the same source surface from multiple threads.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_BlitSurfaceScaled](SDL_BlitSurfaceScaled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

