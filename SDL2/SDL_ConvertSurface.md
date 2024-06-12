###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ConvertSurface

Copy an existing surface to a new surface of the specified format.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
SDL_Surface* SDL_ConvertSurface
    (SDL_Surface * src, const SDL_PixelFormat * fmt, Uint32 flags);
```

## Function Parameters

|                                            |           |                                                                                        |
| ------------------------------------------ | --------- | -------------------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) *               | **src**   | the existing [SDL_Surface](SDL_Surface) structure to convert                           |
| const [SDL_PixelFormat](SDL_PixelFormat) * | **fmt**   | the [SDL_PixelFormat](SDL_PixelFormat) structure that the new surface is optimized for |
| Uint32                                     | **flags** | the flags are unused and should be set to 0; this is a leftover from SDL 1.2's API     |

## Return Value

([SDL_Surface](SDL_Surface) *) Returns the new [SDL_Surface](SDL_Surface)
structure that is created or NULL if it fails; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function is used to optimize images for faster *repeat* blitting. This
is accomplished by converting the original and storing the result as a new
surface. The new, optimized surface can then be used as the source for
future blits, making them faster.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_AllocFormat](SDL_AllocFormat)
- [SDL_ConvertSurfaceFormat](SDL_ConvertSurfaceFormat)
- [SDL_CreateRGBSurface](SDL_CreateRGBSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

