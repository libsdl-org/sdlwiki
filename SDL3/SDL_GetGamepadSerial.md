###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadSerial

Get the serial number of an opened gamepad, if available.

## Header File

Defined in [SDL_gamepad.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
const char * SDL_GetGamepadSerial(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                              |
| --------------- | ---------------------------- |
| **gamepad**     | the gamepad object to query. |

## Return Value

Returns the serial number, or NULL if unavailable.

## Remarks

Returns the serial number of the gamepad, or NULL if it is not available.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

