# SDL_JoystickHasSensor

Return whether a joystick has a particular sensor.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
bool SDL_JoystickHasSensor(SDL_Joystick *joystick, SDL_SensorType type);
```

## Function Parameters

|                                  |              |                              |
| -------------------------------- | ------------ | ---------------------------- |
| [SDL_Joystick](SDL_Joystick) *   | **joystick** | the joystick to query.       |
| [SDL_SensorType](SDL_SensorType) | **type**     | the type of sensor to query. |

## Return Value

(bool) Returns true if the sensor exists, false otherwise.

## Remarks

Sensors are disabled by default and
[SDL_SetJoystickSensorEnabled](SDL_SetJoystickSensorEnabled)() is used to
enable them.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_GetJoystickSensorData](SDL_GetJoystickSensorData)
- [SDL_GetJoystickSensorDataRate](SDL_GetJoystickSensorDataRate)
- [SDL_SetJoystickSensorEnabled](SDL_SetJoystickSensorEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

