# SDL_BlitSurfaceScaled

Perform a scaled blit to a destination surface, which may be of a different format.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_BlitSurfaceScaled(SDL_Surface *src, const SDL_Rect *srcrect, SDL_Surface *dst, const SDL_Rect *dstrect, SDL_ScaleMode scaleMode);
```

## Function Parameters

|                                |               |                                                                                                                                                  |
| ------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Surface](SDL_Surface) *   | **src**       | the [SDL_Surface](SDL_Surface) structure to be copied from.                                                                                      |
| const [SDL_Rect](SDL_Rect) *   | **srcrect**   | the [SDL_Rect](SDL_Rect) structure representing the rectangle to be copied, or NULL to copy the entire surface.                                  |
| [SDL_Surface](SDL_Surface) *   | **dst**       | the [SDL_Surface](SDL_Surface) structure that is the blit target.                                                                                |
| const [SDL_Rect](SDL_Rect) *   | **dstrect**   | the [SDL_Rect](SDL_Rect) structure representing the target rectangle in the destination surface, or NULL to fill the entire destination surface. |
| [SDL_ScaleMode](SDL_ScaleMode) | **scaleMode** | the [SDL_ScaleMode](SDL_ScaleMode) to be used.                                                                                                   |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

The same destination surface should not be used from two threads at once.
It is safe to use the same source surface from multiple threads.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_BlitSurface](SDL_BlitSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

