###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SoftStretchLinear

Perform bilinear scaling between two surfaces of the same format, 32BPP.

## Syntax

```c
int SDL_SoftStretchLinear(SDL_Surface *src,
                    const SDL_Rect *srcrect,
                    SDL_Surface *dst,
                    const SDL_Rect *dstrect);

```

## Function Parameters

|                 |                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------- |
| **src**         | the [SDL_Surface](SDL_Surface.md) structure to be copied from                                      |
| **srcrect**     | the [SDL_Rect](SDL_Rect.md) structure representing the rectangle to be copied                      |
| **dst**         | the [SDL_Surface](SDL_Surface.md) structure that is the blit target                                |
| **dstrect**     | the [SDL_Rect](SDL_Rect.md) structure representing the target rectangle in the destination surface |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
