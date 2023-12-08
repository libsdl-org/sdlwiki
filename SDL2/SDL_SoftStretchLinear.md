###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SoftStretchLinear

Perform bilinear scaling between two surfaces of the same format, 32BPP.

## Syntax

```c
int SDL_SoftStretchLinear(SDL_Surface * src,
                    const SDL_Rect * srcrect,
                    SDL_Surface * dst,
                    const SDL_Rect * dstrect);

```

## Version

This function is available since SDL 2.0.16.

----
[CategoryAPI](CategoryAPI.md)
