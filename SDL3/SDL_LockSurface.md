###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LockSurface

Set up a surface for directly accessing the pixels.

## Syntax

```c
int SDL_LockSurface(SDL_Surface *surface);

```

## Function Parameters

|                 |                                                       |
| --------------- | ----------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) structure to be locked |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Between calls to [SDL_LockSurface](SDL_LockSurface)() /
[SDL_UnlockSurface](SDL_UnlockSurface)(), you can write to and read from
`surface->pixels`, using the pixel format stored in `surface->format`. Once
you are done accessing the surface, you should use
[SDL_UnlockSurface](SDL_UnlockSurface)() to release it.

Not all surfaces require locking. If `SDL_MUSTLOCK(surface)` evaluates to
0, then you can read and write to the surface at any time, and the pixel
format of the surface will not change.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
/* Make the pixels pointer valid in the surface */

SDL_LockSurface(surface);

/* Surface is locked */
/* Direct pixel access on surface here */

SDL_UnlockSurface(surface);

/* Surface is now unlocked */
```

## Related Functions

* [SDL_MUSTLOCK](SDL_MUSTLOCK)
* [SDL_UnlockSurface](SDL_UnlockSurface)

----
[CategoryAPI](CategoryAPI), [CategorySurface](CategorySurface)


