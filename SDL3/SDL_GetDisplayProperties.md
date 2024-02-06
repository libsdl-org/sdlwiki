###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetDisplayProperties

Get the properties associated with a display.

## Syntax

```c
SDL_PropertiesID SDL_GetDisplayProperties(SDL_DisplayID displayID);

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
  true if the display has High Dynamic Range enabled
- [`SDL_PROP_DISPLAY_SDR_WHITE_LEVEL_FLOAT`](SDL_PROP_DISPLAY_SDR_WHITE_LEVEL_FLOAT):
  the luminance, in nits, that SDR white is rendered on this display. If
  this value is not set or is zero, the value 200 is a reasonable default
  when HDR is enabled.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetProperty](SDL_GetProperty)
* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI)

