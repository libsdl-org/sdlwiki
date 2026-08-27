# SDL_JoystickSensorEnabled

Query whether sensor data reporting is enabled for a joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
bool SDL_JoystickSensorEnabled(SDL_Joystick *joystick, SDL_SensorType type);
```

## Function Parameters

|                                  |              |                              |
| -------------------------------- | ------------ | ---------------------------- |
| [SDL_Joystick](SDL_Joystick) *   | **joystick** | the joystick to query.       |
| [SDL_SensorType](SDL_SensorType) | **type**     | the type of sensor to query. |

## Return Value

(bool) Returns true if the sensor is enabled, false otherwise.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_SetJoystickSensorEnabled](SDL_SetJoystickSensorEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

