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

If `surface` has the
[SDL_PROP_SURFACE_ROTATION_FLOAT](SDL_PROP_SURFACE_ROTATION_FLOAT) property
set on it, the new copy will have the adjusted value set: if the rotation
property is 90 and `angle` was 30, the new surface will have a property
value of 60 (that is: to be upright vs gravity, this surface needs to
rotate 60 more degrees). However, note that further rotations on the new
surface in this example will produce unexpected results, since the image
will have resized and padded to accommodate the not-90 degree angle.

## Thread Safety

This function can be called on different threads with different surfaces.

## Version

This function is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

