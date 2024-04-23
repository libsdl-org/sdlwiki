###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_BlitSurface

Performs a fast blit from the source surface to the destination surface.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
#define SDL_BlitSurface SDL_UpperBlit
```

## Return Value

Returns 0 if the blit is successful, otherwise it returns -1.

The blit function should not be called on a locked surface.

The blit semantics for surfaces with and without blending and colorkey are
defined as follows:

## Remarks

This assumes that the source and destination rectangles are the same size.
If either \c srcrect or \c dstrect are NULL, the entire surface (\c src or
\c dst) is copied. The final blit rectangles are saved in \c srcrect and \c
dstrect after all clipping is performed.

## Code Examples

```c
extern SDL_Surface *surface;
extern SDL_Rect source_rect;
SDL_Surface *temp_surface;
     
SDL_BlitSurface(surface, &source_rect, temp_surface, NULL);
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategorySurface](CategorySurface)


