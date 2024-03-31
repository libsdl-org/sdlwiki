###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetGamepadSensorEnabled

Set whether data reporting for a gamepad sensor is enabled.

## Header File

Defined in [SDL_gamepad.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_SetGamepadSensorEnabled(SDL_Gamepad *gamepad, SDL_SensorType type, SDL_bool enabled);

```

## Function Parameters

|                 |                                          |
| --------------- | ---------------------------------------- |
| **gamepad**     | The gamepad to update                    |
| **type**        | The type of sensor to enable/disable     |
| **enabled**     | Whether data reporting should be enabled |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GamepadHasSensor](SDL_GamepadHasSensor)
* [SDL_GamepadSensorEnabled](SDL_GamepadSensorEnabled)

----
[CategoryAPI](CategoryAPI)

