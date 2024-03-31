###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BlitSurface

Performs a fast blit from the source surface to the destination surface.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_BlitSurface(SDL_Surface *src, const SDL_Rect *srcrect, SDL_Surface *dst, SDL_Rect *dstrect);

```

## Function Parameters

|                 |                                                                                                                                                                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **src**         | the [SDL_Surface](SDL_Surface) structure to be copied from                                                                                                                                                                                      |
| **srcrect**     | the [SDL_Rect](SDL_Rect) structure representing the rectangle to be copied, or NULL to copy the entire surface                                                                                                                                  |
| **dst**         | the [SDL_Surface](SDL_Surface) structure that is the blit target                                                                                                                                                                                |
| **dstrect**     | the [SDL_Rect](SDL_Rect) structure representing the x and y position in the destination surface. On input the width and height are ignored (taken from srcrect), and on output this is filled in with the actual rectangle used after clipping. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This assumes that the source and destination rectangles are the same size.
If either `srcrect` or `dstrect` are NULL, the entire surface (`src` or
`dst`) is copied. The final blit rectangles are saved in `srcrect` and
`dstrect` after all clipping is performed.

The blit function should not be called on a locked surface.

The blit semantics for surfaces with and without blending and colorkey are
defined as follows:

```c
   RGBA->RGB:
     Source surface blend mode set to SDL_BLENDMODE_BLEND:
      alpha-blend (using the source alpha-channel and per-surface alpha)
      SDL_SRCCOLORKEY ignored.
    Source surface blend mode set to SDL_BLENDMODE_NONE:
      copy RGB.
      if SDL_SRCCOLORKEY set, only copy the pixels matching the
      RGB values of the source color key, ignoring alpha in the
      comparison.

  RGB->RGBA:
    Source surface blend mode set to SDL_BLENDMODE_BLEND:
      alpha-blend (using the source per-surface alpha)
    Source surface blend mode set to SDL_BLENDMODE_NONE:
      copy RGB, set destination alpha to source per-surface alpha value.
    both:
      if SDL_SRCCOLORKEY set, only copy the pixels matching the
      source color key.

  RGBA->RGBA:
    Source surface blend mode set to SDL_BLENDMODE_BLEND:
      alpha-blend (using the source alpha-channel and per-surface alpha)
      SDL_SRCCOLORKEY ignored.
    Source surface blend mode set to SDL_BLENDMODE_NONE:
      copy all of RGBA to the destination.
      if SDL_SRCCOLORKEY set, only copy the pixels matching the
      RGB values of the source color key, ignoring alpha in the
      comparison.

  RGB->RGB:
    Source surface blend mode set to SDL_BLENDMODE_BLEND:
      alpha-blend (using the source per-surface alpha)
    Source surface blend mode set to SDL_BLENDMODE_NONE:
      copy RGB.
    both:
      if SDL_SRCCOLORKEY set, only copy the pixels matching the
      source color key.
```

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
SDL_BlitSurface(surface, &source_rect, temp_surface, NULL);
```

## Related Functions

* [SDL_BlitSurfaceScaled](SDL_BlitSurfaceScaled)

----
[CategoryAPI](CategoryAPI), [CategorySurface](CategorySurface)


