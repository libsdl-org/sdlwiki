###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetDisplayOrientation

Get the orientation of a display.

## Syntax

```c
SDL_DisplayOrientation SDL_GetDisplayOrientation(int displayIndex);

```

## Function Parameters

|                      |                                   |
| -------------------- | --------------------------------- |
| **displayIndex**     | the index of the display to query |

## Return Value

Returns The [SDL_DisplayOrientation](SDL_DisplayOrientation) enum value of
the display, or `[SDL_ORIENTATION_UNKNOWN](SDL_ORIENTATION_UNKNOWN)` if it
isn't available.

## Version

This function is available since SDL 2.0.9.

## Related Functions

* [SDL_GetNumVideoDisplays](SDL_GetNumVideoDisplays)

----
[CategoryAPI](CategoryAPI)

