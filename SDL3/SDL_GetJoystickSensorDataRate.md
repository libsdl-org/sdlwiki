# SDL_GetJoystickSensorDataRate

Get the data rate (number of events per second) of a joystick sensor.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
float SDL_GetJoystickSensorDataRate(SDL_Joystick *joystick, SDL_SensorType type);
```

## Function Parameters

|                                  |              |                              |
| -------------------------------- | ------------ | ---------------------------- |
| [SDL_Joystick](SDL_Joystick) *   | **joystick** | the joystick to query.       |
| [SDL_SensorType](SDL_SensorType) | **type**     | the type of sensor to query. |

## Return Value

(float) Returns the data rate, or 0.0f if the data rate is not available.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

