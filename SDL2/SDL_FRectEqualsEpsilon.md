###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FRectEqualsEpsilon

Returns true if the two rectangles are equal, within some given epsilon.

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rect.h)

## Syntax

```c
SDL_FORCE_INLINE SDL_bool SDL_FRectEqualsEpsilon(const SDL_FRect *a, const SDL_FRect *b, const float epsilon);
```

## Version

This function is available since SDL 2.0.22.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

