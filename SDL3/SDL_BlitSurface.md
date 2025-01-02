###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_BlitSurface

Performs a fast blit from the source surface to the destination surface with clipping.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_BlitSurface(SDL_Surface *src, const SDL_Rect *srcrect, SDL_Surface *dst, const SDL_Rect *dstrect);
```

## Function Parameters

|                              |             |                                                                                                                                                                                                                                                                                                |
| ---------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **src**     | the [SDL_Surface](SDL_Surface) structure to be copied from.                                                                                                                                                                                                                                    |
| const [SDL_Rect](SDL_Rect) * | **srcrect** | the [SDL_Rect](SDL_Rect) structure representing the rectangle to be copied, or NULL to copy the entire surface.                                                                                                                                                                                |
| [SDL_Surface](SDL_Surface) * | **dst**     | the [SDL_Surface](SDL_Surface) structure that is the blit target.                                                                                                                                                                                                                              |
| const [SDL_Rect](SDL_Rect) * | **dstrect** | the [SDL_Rect](SDL_Rect) structure representing the x and y position in the destination surface, or NULL for (0,0). The width and height are ignored, and are copied from `srcrect`. If you want a specific width and height, you should use [SDL_BlitSurfaceScaled](SDL_BlitSurfaceScaled)(). |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If either `srcrect` or `dstrect` are NULL, the entire surface (`src` or
`dst`) is copied while ensuring clipping to `dst->clip_rect`.

The final blit rectangles are saved in `srcrect` and `dstrect` after all
clipping is performed.

The blit function should not be called on a locked surface.

The blit semantics for surfaces with and without blending and colorkey are
defined as follows:

```
   RGBA->RGB:
     Source surface blend mode set to SDL_BLENDMODE_BLEND:
      alpha-blend (using the source alpha-channel and per-surface alpha)
      SDL_SRCCOLORKEY ignored.
    Source surface blend mode set to SDL_BLENDMODE_NONE:
      copy RGB.
      if SDL_SRCCOLORKEY set, only copy the pixels that do not match the
      RGB values of the source color key, ignoring alpha in the
      comparison.

  RGB->RGBA:
    Source surface blend mode set to SDL_BLENDMODE_BLEND:
      alpha-blend (using the source per-surface alpha)
    Source surface blend mode set to SDL_BLENDMODE_NONE:
      copy RGB, set destination alpha to source per-surface alpha value.
    both:
      if SDL_SRCCOLORKEY set, only copy the pixels that do not match the
      source color key.

  RGBA->RGBA:
    Source surface blend mode set to SDL_BLENDMODE_BLEND:
      alpha-blend (using the source alpha-channel and per-surface alpha)
      SDL_SRCCOLORKEY ignored.
    Source surface blend mode set to SDL_BLENDMODE_NONE:
      copy all of RGBA to the destination.
      if SDL_SRCCOLORKEY set, only copy the pixels that do not match the
      RGB values of the source color key, ignoring alpha in the
      comparison.

  RGB->RGB:
    Source surface blend mode set to SDL_BLENDMODE_BLEND:
      alpha-blend (using the source per-surface alpha)
    Source surface blend mode set to SDL_BLENDMODE_NONE:
      copy RGB.
    both:
      if SDL_SRCCOLORKEY set, only copy the pixels that do not match the
      source color key.
```

## Thread Safety

The same destination surface should not be used from two threads at once.
It is safe to use the same source surface from multiple threads.

## Version

This function is available since SDL 3.1.3.

## Code Examples

```c
SDL_Surface *surface;
SDL_Rect source_rect;
SDL_Surface *temp_surface;

SDL_BlitSurface(surface, &source_rect, temp_surface, NULL);
```

## See Also

- [SDL_BlitSurfaceScaled](SDL_BlitSurfaceScaled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

