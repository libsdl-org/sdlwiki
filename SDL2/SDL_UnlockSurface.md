###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UnlockSurface

Release a surface after directly accessing the pixels.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
void SDL_UnlockSurface(SDL_Surface * surface);

```

## Function Parameters

|                 |                                                         |
| --------------- | ------------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) structure to be unlocked |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_LockSurface](SDL_LockSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


