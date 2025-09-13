# SDL_SoftStretchLinear

Perform bilinear scaling between two surfaces of the same format, 32BPP.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
int SDL_SoftStretchLinear(SDL_Surface * src,
                    const SDL_Rect * srcrect,
                    SDL_Surface * dst,
                    const SDL_Rect * dstrect);
```

## Function Parameters

|                              |             |                                      |
| ---------------------------- | ----------- | ------------------------------------ |
| [SDL_Surface](SDL_Surface) * | **src**     | the surface to be copied from.       |
| const [SDL_Rect](SDL_Rect) * | **srcrect** | the rectangle to be copied.          |
| [SDL_Surface](SDL_Surface) * | **dst**     | the surface that is the blit target. |
| const [SDL_Rect](SDL_Rect) * | **dstrect** | the rectangle that is copied into.   |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.16.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

