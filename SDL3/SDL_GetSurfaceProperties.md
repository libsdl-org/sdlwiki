# SDL_GetSurfaceProperties

Get the properties associated with a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_PropertiesID SDL_GetSurfaceProperties(SDL_Surface *surface);
```

## Function Parameters

|                              |             |                                                    |
| ---------------------------- | ----------- | -------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to query. |

## Return Value

([SDL_PropertiesID](SDL_PropertiesID)) Returns a valid property ID on
success or 0 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

The following properties are understood by SDL:

- [`SDL_PROP_SURFACE_SDR_WHITE_POINT_FLOAT`](SDL_PROP_SURFACE_SDR_WHITE_POINT_FLOAT):
  for HDR10 and floating point surfaces, this defines the value of 100%
  diffuse white, with higher values being displayed in the High Dynamic
  Range headroom. This defaults to 203 for HDR10 surfaces and 1.0 for
  floating point surfaces.
- [`SDL_PROP_SURFACE_HDR_HEADROOM_FLOAT`](SDL_PROP_SURFACE_HDR_HEADROOM_FLOAT):
  for HDR10 and floating point surfaces, this defines the maximum dynamic
  range used by the content, in terms of the SDR white point. This defaults
  to 0.0, which disables tone mapping.
- [`SDL_PROP_SURFACE_TONEMAP_OPERATOR_STRING`](SDL_PROP_SURFACE_TONEMAP_OPERATOR_STRING):
  the tone mapping operator used when compressing from a surface with high
  dynamic range to another with lower dynamic range. Currently this
  supports "chrome", which uses the same tone mapping that Chrome uses for
  HDR content, the form "*=N", where N is a floating point scale factor
  applied in linear space, and "none", which disables tone mapping. This
  defaults to "chrome".
- [`SDL_PROP_SURFACE_HOTSPOT_X_NUMBER`](SDL_PROP_SURFACE_HOTSPOT_X_NUMBER):
  the hotspot pixel offset from the left edge of the image, if this surface
  is being used as a cursor.
- [`SDL_PROP_SURFACE_HOTSPOT_Y_NUMBER`](SDL_PROP_SURFACE_HOTSPOT_Y_NUMBER):
  the hotspot pixel offset from the top edge of the image, if this surface
  is being used as a cursor.
- [`SDL_PROP_SURFACE_ROTATION_FLOAT`](SDL_PROP_SURFACE_ROTATION_FLOAT): the
  number of degrees a surface's data is meant to be rotated clockwise to
  make the image right-side up. Default 0. This is used by the camera API,
  if a mobile device is oriented differently than what its camera provides
  (i.e. - the camera always provides portrait images but the phone is being
  held in landscape orientation). Since SDL 3.4.0.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

