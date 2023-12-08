###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FreeSurface

Free an RGB surface.

## Syntax

```c
void SDL_FreeSurface(SDL_Surface * surface);

```

## Function Parameters

|                 |                                         |
| --------------- | --------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface.md) to free. |

## Remarks

It is safe to pass NULL to this function.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateRGBSurface](SDL_CreateRGBSurface.md)
* [SDL_CreateRGBSurfaceFrom](SDL_CreateRGBSurfaceFrom.md)
* [SDL_LoadBMP](SDL_LoadBMP.md)
* [SDL_LoadBMP_RW](SDL_LoadBMP_RW.md)

----
[CategoryAPI](CategoryAPI.md)
