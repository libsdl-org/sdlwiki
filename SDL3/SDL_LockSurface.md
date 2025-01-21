###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_LockSurface

Set up a surface for directly accessing the pixels.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_LockSurface(SDL_Surface *surface);
```

## Function Parameters

|                              |             |                                                        |
| ---------------------------- | ----------- | ------------------------------------------------------ |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to be locked. |

## Return Value

(bool) Returns true on success or false on failure; call
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

This function is available since SDL 3.2.0.

## See Also

- [SDL_MUSTLOCK](SDL_MUSTLOCK)
- [SDL_UnlockSurface](SDL_UnlockSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

