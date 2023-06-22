###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetClosestFullscreenDisplayMode

Get the closest match to the requested display mode.

## Syntax

```c
const SDL_DisplayMode* SDL_GetClosestFullscreenDisplayMode(SDL_DisplayID displayID, int w, int h, float refresh_rate, SDL_bool include_high_density_modes);

```

## Function Parameters

|                                    |                                                                                    |
| ---------------------------------- | ---------------------------------------------------------------------------------- |
| **displayID**                      | the instance ID of the display to query                                            |
| **w**                              | the width in pixels of the desired display mode                                    |
| **h**                              | the height in pixels of the desired display mode                                   |
| **refresh_rate**                   | the refresh rate of the desired display mode, or 0.0f for the desktop refresh rate |
| **include_high_density_modes**     | Boolean to include high density modes in the search                                |

## Return Value

Returns a pointer to the closest display mode equal to or larger than the
desired mode, or NULL on error; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

The available display modes are scanned and `closest` is filled in with the
closest mode matching the requested mode and returned. The mode format and
refresh rate default to the desktop mode if they are set to 0. The modes
are scanned with size being first priority, format being second priority,
and finally checking the refresh rate. If all the available modes are too
small, then NULL is returned.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetDisplays](SDL_GetDisplays)
* [SDL_GetFullscreenDisplayModes](SDL_GetFullscreenDisplayModes)

----
[CategoryAPI](CategoryAPI)

