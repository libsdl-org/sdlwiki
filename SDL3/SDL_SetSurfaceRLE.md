###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetSurfaceRLE

Set the RLE acceleration hint for a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_SetSurfaceRLE(SDL_Surface *surface, bool enabled);
```

## Function Parameters

|                              |             |                                                       |
| ---------------------------- | ----------- | ----------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to optimize. |
| bool                         | **enabled** | true to enable RLE acceleration, false to disable it. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If RLE is enabled, color key and alpha blending blits are much faster, but
the surface must be locked before directly accessing the pixels.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_BlitSurface](SDL_BlitSurface)
- [SDL_LockSurface](SDL_LockSurface)
- [SDL_UnlockSurface](SDL_UnlockSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

