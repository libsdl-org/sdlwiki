# SDL_SoftStretch

Perform a fast, low quality, stretch blit between two surfaces of the same format.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
int SDL_SoftStretch(SDL_Surface * src,
                    const SDL_Rect * srcrect,
                    SDL_Surface * dst,
                    const SDL_Rect * dstrect);
```

## Remarks

Please use [SDL_BlitScaled](SDL_BlitScaled)() instead.

## Version

This function is available since SDL 2.0.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

