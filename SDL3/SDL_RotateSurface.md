# SDL_RotateSurface

Return a copy of a surface rotated clockwise a number of degrees.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_Surface * SDL_RotateSurface(SDL_Surface *surface, float angle);
```

## Function Parameters

|                              |             |                                 |
| ---------------------------- | ----------- | ------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the surface to rotate.          |
| float                        | **angle**   | the rotation angle, in degrees. |

## Return Value

([SDL_Surface](SDL_Surface) *) Returns a rotated copy of the surface or
NULL on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The angle of rotation can be negative for counter-clockwise rotation.

When the rotation isn't a multiple of 90 degrees, the resulting surface is
larger than the original, with the background filled in with the colorkey,
if available, or RGBA 255/255/255/0 if not.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

