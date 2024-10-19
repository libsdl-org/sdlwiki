###### (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)
# SDL_BlitSurface

Performs a fast blit from the source surface to the destination surface.
This is defined as a macro to [SDL_UpperBlit](SDL_UpperBlit) to be less confusing.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
#define SDL_BlitSurface SDL_UpperBlit
```
Processes to:
```c
int SDL_UpperBlit
    (SDL_Surface * src, const SDL_Rect * srcrect,
     SDL_Surface * dst, SDL_Rect * dstrect);
```

## Return Value

Returns 0 if the blit is successful, otherwise it returns -1.

## Remarks

This assumes that the source and destination rectangles are the same size.
If either `srcrect` or `dstrect` are NULL, the entire surface (`src` or
`dst`) is copied. The final blit rectangles are saved in `srcrect` and
`dstrect` after all clipping is performed.

The blit function should not be called on a locked surface.

The blit semantics for surfaces with and without blending and colorkey are
defined as follows:

## RGBA to RGB:
- Source surface blend mode set to SDL_BLENDMODE_BLEND:
  * alpha-blend (using the source alpha-channel and per-surface alpha)
SDL_SRCCOLORKEY ignored.
- Source surface blend mode set to SDL_BLENDMODE_NONE:
  * copy RGB.
  * if SDL_SRCCOLORKEY set, only copy the pixels matching the
RGB values of the source color key, ignoring alpha in the
comparison.

## RGB to RGBA:
- Source surface blend mode set to SDL_BLENDMODE_BLEND:
  * alpha-blend (using the source per-surface alpha)
- Source surface blend mode set to SDL_BLENDMODE_NONE:
  * copy RGB, set destination alpha to source per-surface alpha value.
- both:
  * if SDL_SRCCOLORKEY set, only copy the pixels matching the
source color key.

## RGBA to RGBA:
- Source surface blend mode set to SDL_BLENDMODE_BLEND:
  * alpha-blend (using the source alpha-channel and per-surface alpha)
  * SDL_SRCCOLORKEY ignored.
- Source surface blend mode set to SDL_BLENDMODE_NONE:
  * copy all of RGBA to the destination.
  * if SDL_SRCCOLORKEY set, only copy the pixels matching the
RGB values of the source color key, ignoring alpha in the
comparison.

## RGB to RGB:
- Source surface blend mode set to SDL_BLENDMODE_BLEND:
  * alpha-blend (using the source per-surface alpha)
- Source surface blend mode set to SDL_BLENDMODE_NONE:
  * copy RGB.
- both:
  * if SDL_SRCCOLORKEY set, only copy the pixels matching the
source color key.

You should call [SDL_BlitSurface](SDL_BlitSurface)() unless you know
exactly how SDL blitting works internally and how to use the other blit
functions.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategorySurface](CategorySurface)

