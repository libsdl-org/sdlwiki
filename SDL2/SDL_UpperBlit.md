###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UpperBlit

Perform a fast blit from the source surface to the destination surface.

## Syntax

```c
int SDL_UpperBlit
    (SDL_Surface * src, const SDL_Rect * srcrect,
     SDL_Surface * dst, SDL_Rect * dstrect);

```

## Remarks

[SDL_UpperBlit](SDL_UpperBlit.md)() has been replaced by
[SDL_BlitSurface](SDL_BlitSurface.md)(), which is merely a macro for this
function with a less confusing name.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_BlitSurface](SDL_BlitSurface.md)

----
[CategoryAPI](CategoryAPI.md)
