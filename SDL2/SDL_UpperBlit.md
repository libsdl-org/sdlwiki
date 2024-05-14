###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UpperBlit

Perform a fast blit from the source surface to the destination surface.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
int SDL_UpperBlit
    (SDL_Surface * src, const SDL_Rect * srcrect,
     SDL_Surface * dst, SDL_Rect * dstrect);

```

## Remarks

[SDL_UpperBlit](SDL_UpperBlit)() has been replaced by
[SDL_BlitSurface](SDL_BlitSurface)(), which is merely a macro for this
function with a less confusing name.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_BlitSurface](SDL_BlitSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

