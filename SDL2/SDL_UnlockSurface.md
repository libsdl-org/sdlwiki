###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UnlockSurface

Release a surface after directly accessing the pixels.

## Syntax

```c
void SDL_UnlockSurface(SDL_Surface * surface);

```

## Function Parameters

|                 |                                                         |
| --------------- | ------------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface.md) structure to be unlocked |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_LockSurface](SDL_LockSurface.md)

----
[CategoryAPI](CategoryAPI.md)
