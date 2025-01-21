###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_BlitSurfaceUnchecked

Perform low-level surface blitting only.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_BlitSurfaceUnchecked(SDL_Surface *src, const SDL_Rect *srcrect, SDL_Surface *dst, const SDL_Rect *dstrect);
```

## Function Parameters

|                              |             |                                                                                                                   |
| ---------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **src**     | the [SDL_Surface](SDL_Surface) structure to be copied from.                                                       |
| const [SDL_Rect](SDL_Rect) * | **srcrect** | the [SDL_Rect](SDL_Rect) structure representing the rectangle to be copied, may not be NULL.                      |
| [SDL_Surface](SDL_Surface) * | **dst**     | the [SDL_Surface](SDL_Surface) structure that is the blit target.                                                 |
| const [SDL_Rect](SDL_Rect) * | **dstrect** | the [SDL_Rect](SDL_Rect) structure representing the target rectangle in the destination surface, may not be NULL. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is a semi-private blit function and it performs low-level surface
blitting, assuming the input rectangles have already been clipped.

## Thread Safety

The same destination surface should not be used from two threads at once.
It is safe to use the same source surface from multiple threads.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_BlitSurface](SDL_BlitSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

