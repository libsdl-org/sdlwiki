###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetGamepadSensorEnabled

Set whether data reporting for a gamepad sensor is enabled.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
bool SDL_SetGamepadSensorEnabled(SDL_Gamepad *gamepad, SDL_SensorType type, bool enabled);
```

## Function Parameters

|                                  |             |                                           |
| -------------------------------- | ----------- | ----------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) *     | **gamepad** | the gamepad to update.                    |
| [SDL_SensorType](SDL_SensorType) | **type**    | the type of sensor to enable/disable.     |
| bool                             | **enabled** | whether data reporting should be enabled. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GamepadHasSensor](SDL_GamepadHasSensor)
- [SDL_GamepadSensorEnabled](SDL_GamepadSensorEnabled)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

