# SDL_GamepadSensorEnabled

Query whether sensor data reporting is enabled for a gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
bool SDL_GamepadSensorEnabled(SDL_Gamepad *gamepad, SDL_SensorType type);
```

## Function Parameters

|                                  |             |                              |
| -------------------------------- | ----------- | ---------------------------- |
| [SDL_Gamepad](SDL_Gamepad) *     | **gamepad** | the gamepad to query.        |
| [SDL_SensorType](SDL_SensorType) | **type**    | the type of sensor to query. |

## Return Value

(bool) Returns true if the sensor is enabled, false otherwise.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetGamepadSensorEnabled](SDL_SetGamepadSensorEnabled)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

