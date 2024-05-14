###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UpperBlitScaled

Perform a scaled surface copy to a destination surface.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
int SDL_UpperBlitScaled
    (SDL_Surface * src, const SDL_Rect * srcrect,
    SDL_Surface * dst, SDL_Rect * dstrect);


#define SDL_BlitScaled SDL_UpperBlitScaled
```

## Remarks

[SDL_UpperBlitScaled](SDL_UpperBlitScaled)() has been replaced by
[SDL_BlitScaled](SDL_BlitScaled)(), which is merely a macro for this
function with a less confusing name.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_BlitScaled](SDL_BlitScaled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

