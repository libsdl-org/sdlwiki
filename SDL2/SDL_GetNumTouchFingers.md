###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetNumTouchFingers

Get the number of active fingers for a given touch device.

## Header File

Defined in [SDL_touch.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_touch.h)

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
0 on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_GetTouchFinger](SDL_GetTouchFinger)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

