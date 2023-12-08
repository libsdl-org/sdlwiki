###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UpperBlitScaled

Perform a scaled surface copy to a destination surface.

## Syntax

```c
int SDL_UpperBlitScaled
    (SDL_Surface * src, const SDL_Rect * srcrect,
    SDL_Surface * dst, SDL_Rect * dstrect);

```

## Remarks

[SDL_UpperBlitScaled](SDL_UpperBlitScaled.md)() has been replaced by
[SDL_BlitScaled](SDL_BlitScaled.md)(), which is merely a macro for this
function with a less confusing name.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_BlitScaled](SDL_BlitScaled.md)

----
[CategoryAPI](CategoryAPI.md)
