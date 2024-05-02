###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetDisplayProperties

Get the properties associated with a display.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_PropertiesID SDL_GetDisplayProperties(SDL_DisplayID displayID);


#define SDL_PROP_DISPLAY_HDR_ENABLED_BOOLEAN            "SDL.display.HDR_enabled"
#define SDL_PROP_DISPLAY_SDR_WHITE_POINT_FLOAT          "SDL.display.SDR_white_point"
#define SDL_PROP_DISPLAY_HDR_HEADROOM_FLOAT             "SDL.display.HDR_headroom"
```

## Function Parameters

|                   |                                         |
| ----------------- | --------------------------------------- |
| **displayID**     | the instance ID of the display to query |

## Return Value

Returns a valid property ID on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The following read-only properties are provided by SDL:

- [`SDL_PROP_DISPLAY_HDR_ENABLED_BOOLEAN`](SDL_PROP_DISPLAY_HDR_ENABLED_BOOLEAN):
  true if the display has HDR headroom above the SDR white point. This
  property can change dynamically when
  [SDL_EVENT_DISPLAY_HDR_STATE_CHANGED](SDL_EVENT_DISPLAY_HDR_STATE_CHANGED)
  is sent.
- [`SDL_PROP_DISPLAY_SDR_WHITE_POINT_FLOAT`](SDL_PROP_DISPLAY_SDR_WHITE_POINT_FLOAT):
  the value of SDR white in the
  [SDL_COLORSPACE_SRGB_LINEAR](SDL_COLORSPACE_SRGB_LINEAR) colorspace. On
  Windows this corresponds to the SDR white level in scRGB colorspace, and
  on Apple platforms this is always 1.0 for EDR content. This property can
  change dynamically when
  [SDL_EVENT_DISPLAY_HDR_STATE_CHANGED](SDL_EVENT_DISPLAY_HDR_STATE_CHANGED)
  is sent.
- [`SDL_PROP_DISPLAY_HDR_HEADROOM_FLOAT`](SDL_PROP_DISPLAY_HDR_HEADROOM_FLOAT):
  the additional high dynamic range that can be displayed, in terms of the
  SDR white point. When HDR is not enabled, this will be 1.0. This property
  can change dynamically when
  [SDL_EVENT_DISPLAY_HDR_STATE_CHANGED](SDL_EVENT_DISPLAY_HDR_STATE_CHANGED)
  is sent.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetProperty](SDL_GetProperty)
* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

