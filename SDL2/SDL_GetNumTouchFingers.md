###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetNumTouchFingers

Get the number of active fingers for a given touch device.

## Syntax

```c
int SDL_GetNumTouchFingers(SDL_TouchID touchID);

```

## Function Parameters

|                 |                          |
| --------------- | ------------------------ |
| **touchID**     | the ID of a touch device |

## Return Value

Returns the number of active fingers for a given touch device on success or
0 on failure; call [SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetTouchFinger](SDL_GetTouchFinger.md)

----
[CategoryAPI](CategoryAPI.md)
