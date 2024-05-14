###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GamepadHasSensor

Return whether a gamepad has a particular sensor.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_bool SDL_GamepadHasSensor(SDL_Gamepad *gamepad, SDL_SensorType type);

```

## Function Parameters

|                 |                             |
| --------------- | --------------------------- |
| **gamepad**     | The gamepad to query        |
| **type**        | The type of sensor to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the sensor exists, [SDL_FALSE](SDL_FALSE)
otherwise.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetGamepadSensorData](SDL_GetGamepadSensorData)
- [SDL_GetGamepadSensorDataRate](SDL_GetGamepadSensorDataRate)
- [SDL_SetGamepadSensorEnabled](SDL_SetGamepadSensorEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

