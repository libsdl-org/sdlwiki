###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
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

- [`SDL_PROP_DISPLAY_KMSDRM_PANEL_ORIENTATION_NUMBER`](SDL_PROP_DISPLAY_KMSDRM_PANEL_ORIENTATION_NUMBER):
  the "panel orientation" property for the display in degrees of clockwise
  rotation. Note that this is provided only as a hint, and the application
  is responsible for any coordinate transformations needed to conform to
  the requested display orientation.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.1.3.

## Code Examples

```c
// Example program
// Use SDL3 to check whether displays have HDR enabled

#include <SDL3/SDL_log.h>
#include <SDL3/SDL_main.h>
#include <SDL3/SDL_stdinc.h>
#include <SDL3/SDL_video.h>

int
main(int argc, char** argv)
{
  if (!SDL_Init(SDL_INIT_VIDEO)) {
    SDL_Log("Unable to initialize SDL: %s", SDL_GetError());
    return 0;
  }

  SDL_Log("SDL initialized");

  int num_displays;
  SDL_DisplayID *displays = SDL_GetDisplays(&num_displays);

  for(int i = 0; i < num_displays; i++) {
    SDL_PropertiesID prop_id = SDL_GetDisplayProperties(displays[i]);

    if(!SDL_GetBooleanProperty(prop_id, SDL_PROP_DISPLAY_HDR_ENABLED_BOOLEAN, false)) {
      SDL_Log("Display with ID %"SDL_PRIu32 " does not have HDR enabled.", displays[i]);
    } else {
      SDL_Log("Display with ID %"SDL_PRIu32 " has HDR enabled.", displays[i]);
    }
  }

  SDL_free(displays);

  return 0;
}
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

