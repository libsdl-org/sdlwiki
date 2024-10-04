###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_CreateSurface

Allocate a new surface with a specific pixel format.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_Surface * SDL_CreateSurface(int width, int height, SDL_PixelFormat format);
```

## Function Parameters

|                                    |            |                                                                            |
| ---------------------------------- | ---------- | -------------------------------------------------------------------------- |
| int                                | **width**  | the width of the surface.                                                  |
| int                                | **height** | the height of the surface.                                                 |
| [SDL_PixelFormat](SDL_PixelFormat) | **format** | the [SDL_PixelFormat](SDL_PixelFormat) for the new surface's pixel format. |

## Return Value

([SDL_Surface](SDL_Surface) *) Returns the new [SDL_Surface](SDL_Surface)
structure that is created or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The pixels of the new surface are initialized to zero.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateSurfaceFrom](SDL_CreateSurfaceFrom)
- [SDL_DestroySurface](SDL_DestroySurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

