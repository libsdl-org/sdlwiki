###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetDisplayProperties

Get the properties associated with a display.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_PropertiesID SDL_GetDisplayProperties(SDL_DisplayID displayID);
```

## Function Parameters

|                                |               |                                          |
| ------------------------------ | ------------- | ---------------------------------------- |
| [SDL_DisplayID](SDL_DisplayID) | **displayID** | the instance ID of the display to query. |

## Return Value

([SDL_PropertiesID](SDL_PropertiesID)) Returns a valid property ID on
success or 0 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

The following read-only properties are provided by SDL:

- [`SDL_PROP_DISPLAY_HDR_ENABLED_BOOLEAN`](SDL_PROP_DISPLAY_HDR_ENABLED_BOOLEAN):
  true if the display has HDR headroom above the SDR white point. This is
  for informational and diagnostic purposes only, as not all platforms
  provide this information at the display level.

On KMS/DRM:

- [`SDL_PROP_DISPLAY_KMSDRM_ORIENTATION_NUMBER`](SDL_PROP_DISPLAY_KMSDRM_ORIENTATION_NUMBER):
  the "panel orientation" property for the display in degrees of clockwise
  rotation. Note that this is provided only as a hint, and the application
  is responsible for any coordinate transformations needed to conform to
  the requested display orientation.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetProperty](SDL_GetProperty)
- [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

