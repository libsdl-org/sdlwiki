###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SoftStretch

Perform stretch blit between two surfaces of the same format.

## Syntax

```c
int SDL_SoftStretch(SDL_Surface *src, const SDL_Rect *srcrect, SDL_Surface *dst, const SDL_Rect *dstrect, SDL_ScaleMode scaleMode);

```

## Function Parameters

|                   |                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| **src**           | the [SDL_Surface](SDL_Surface) structure to be copied from                                      |
| **srcrect**       | the [SDL_Rect](SDL_Rect) structure representing the rectangle to be copied                      |
| **dst**           | the [SDL_Surface](SDL_Surface) structure that is the blit target                                |
| **dstrect**       | the [SDL_Rect](SDL_Rect) structure representing the target rectangle in the destination surface |
| **scaleMode**     | scale algorithm to be used                                                                      |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Using [SDL_SCALEMODE_NEAREST](SDL_SCALEMODE_NEAREST): fast, low quality.
Using [SDL_SCALEMODE_LINEAR](SDL_SCALEMODE_LINEAR): bilinear scaling,
slower, better quality, only 32BPP.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_BlitSurfaceScaled](SDL_BlitSurfaceScaled)

----
[CategoryAPI](CategoryAPI)

