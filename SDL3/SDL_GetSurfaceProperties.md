###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSurfaceProperties

Get the properties associated with a surface.

## Syntax

```c
SDL_PropertiesID SDL_GetSurfaceProperties(SDL_Surface *surface);

```

## Function Parameters

|                 |                                                   |
| --------------- | ------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) structure to query |

## Return Value

Returns a valid property ID on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The following properties are understood by SDL:

- [`SDL_PROP_SURFACE_COLORSPACE_NUMBER`](SDL_PROP_SURFACE_COLORSPACE_NUMBER):
  an [SDL_ColorSpace](SDL_ColorSpace) value describing the surface
  colorspace, defaults to
  [SDL_COLORSPACE_SRGB_LINEAR](SDL_COLORSPACE_SRGB_LINEAR) for floating
  point formats, [SDL_COLORSPACE_HDR10](SDL_COLORSPACE_HDR10) for 10-bit
  formats, [SDL_COLORSPACE_SRGB](SDL_COLORSPACE_SRGB) for other RGB
  surfaces and [SDL_COLORSPACE_BT709_FULL](SDL_COLORSPACE_BT709_FULL) for
  YUV surfaces.
- [`SDL_PROP_SURFACE_MAXCLL_NUMBER`](SDL_PROP_SURFACE_MAXCLL_NUMBER):
  MaxCLL (Maximum Content Light Level) indicates the maximum light level of
  any single pixel (in cd/m2 or nits) of the content. MaxCLL is usually
  measured off the final delivered content after mastering. If one uses the
  full light level of the HDR mastering display and adds a hard clip at its
  maximum value, MaxCLL would be equal to the peak luminance of the
  mastering monitor. This defaults to 400 for HDR10 surfaces.
- [`SDL_PROP_SURFACE_MAXFALL_NUMBER`](SDL_PROP_SURFACE_MAXFALL_NUMBER):
  MaxFALL (Maximum Frame Average Light Level) indicates the maximum value
  of the frame average light level (in cd/m2 or nits) of the content.
  MaxFALL is calculated by averaging the decoded luminance values of all
  the pixels within a frame. MaxFALL is usually much lower than MaxCLL.
- [`SDL_PROP_SURFACE_SDR_WHITE_POINT_FLOAT`](SDL_PROP_SURFACE_SDR_WHITE_POINT_FLOAT):
  for HDR10 and floating point surfaces, this defines the value of 100%
  diffuse white, with higher values being displayed in the High Dynamic
  Range headroom. This defaults to 100 for HDR10 surfaces and 1.0 for other
  surfaces.
- [`SDL_PROP_SURFACE_HDR_HEADROOM_FLOAT`](SDL_PROP_SURFACE_HDR_HEADROOM_FLOAT):
  for HDR10 and floating point surfaces, this defines the maximum dynamic
  range used by the content, in terms of the SDR white point. This defaults
  to [SDL_PROP_SURFACE_MAXCLL_NUMBER](SDL_PROP_SURFACE_MAXCLL_NUMBER) /
  [SDL_PROP_SURFACE_SDR_WHITE_POINT_FLOAT](SDL_PROP_SURFACE_SDR_WHITE_POINT_FLOAT),
  or 4.0, for HDR10 surfaces.
- [`SDL_PROP_SURFACE_TONEMAP_OPERATOR_STRING`](SDL_PROP_SURFACE_TONEMAP_OPERATOR_STRING):
  the tone mapping operator used when compressing from a surface with high
  dynamic range to another with lower dynamic range. Currently this
  supports "chrome", which uses the same tone mapping that Chrome uses for
  HDR content, the form "*=N", where N is a floating point scale factor
  applied in linear space, and "none", which disables tone mapping. This
  defaults to "chrome".

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetProperty](SDL_GetProperty)
* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI)
