###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCurrentDisplayOrientation

Get the orientation of a display.

## Syntax

```c
SDL_DisplayOrientation SDL_GetCurrentDisplayOrientation(SDL_DisplayID displayID);

```

## Function Parameters

|                   |                                         |
| ----------------- | --------------------------------------- |
| **displayID**     | the instance ID of the display to query |

## Return Value

Returns The [SDL_DisplayOrientation](SDL_DisplayOrientation) enum value of
the display, or [`SDL_ORIENTATION_UNKNOWN`](SDL_ORIENTATION_UNKNOWN) if it
isn't available.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetDisplays](SDL_GetDisplays)

----
[CategoryAPI](CategoryAPI)

