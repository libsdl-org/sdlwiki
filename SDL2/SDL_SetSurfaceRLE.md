###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetSurfaceRLE

Set the RLE acceleration hint for a surface.

## Syntax

```c
int SDL_SetSurfaceRLE(SDL_Surface * surface,
                      int flag);

```

## Function Parameters

|                 |                                                      |
| --------------- | ---------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface.md) structure to optimize |
| **flag**        | 0 to disable, non-zero to enable RLE acceleration    |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

If RLE is enabled, color key and alpha blending blits are much faster, but
the surface must be locked before directly accessing the pixels.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_BlitSurface](SDL_BlitSurface.md)
* [SDL_LockSurface](SDL_LockSurface.md)
* [SDL_UnlockSurface](SDL_UnlockSurface.md)

----
[CategoryAPI](CategoryAPI.md)
