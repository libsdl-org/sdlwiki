###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LockSurface

Set up a surface for directly accessing the pixels.

## Syntax

```c
int SDL_LockSurface(SDL_Surface * surface);

```

## Function Parameters

|                 |                                                       |
| --------------- | ----------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface.md) structure to be locked |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Between calls to [SDL_LockSurface](SDL_LockSurface.md)() /
[SDL_UnlockSurface](SDL_UnlockSurface.md)(), you can write to and read from
`surface->pixels`, using the pixel format stored in `surface->format`. Once
you are done accessing the surface, you should use
[SDL_UnlockSurface](SDL_UnlockSurface.md)() to release it.

Not all surfaces require locking. If `SDL_MUSTLOCK(surface)` evaluates to
0, then you can read and write to the surface at any time, and the pixel
format of the surface will not change.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_MUSTLOCK](SDL_MUSTLOCK.md)
* [SDL_UnlockSurface](SDL_UnlockSurface.md)

----
[CategoryAPI](CategoryAPI.md)
