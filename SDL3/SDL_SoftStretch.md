###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SoftStretch

Perform a fast, low quality, stretch blit between two surfaces of the same format.

## Syntax

```c
int SDL_SoftStretch(SDL_Surface *src,
                    const SDL_Rect *srcrect,
                    SDL_Surface *dst,
                    const SDL_Rect *dstrect);

```

## Function Parameters

|                 |                                                                                   |
| --------------- | --------------------------------------------------------------------------------- |
| **src**         | the [SDL_Surface](SDL_Surface) structure to be copied from                        |
| **srcrect**     | the [SDL_Rect](SDL_Rect) structure representing the rectangle to be copied        |
| **dst**         | the [SDL_Surface](SDL_Surface) structure that is the blit target                  |
| **dstrect**     | the [SDL_Rect](SDL_Rect) structure representing the rectangle that is copied into |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

**WARNING**: Please use [SDL_BlitScaled](SDL_BlitScaled)() instead.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

