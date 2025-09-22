# SDL_SendJoystickVirtualSensorData

Send a sensor update for an opened virtual joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
bool SDL_SendJoystickVirtualSensorData(SDL_Joystick *joystick, SDL_SensorType type, Uint64 sensor_timestamp, const float *data, int num_values);
```

## Function Parameters

|                                  |                      |                                                                       |
| -------------------------------- | -------------------- | --------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) *   | **joystick**         | the virtual joystick on which to set state.                           |
| [SDL_SensorType](SDL_SensorType) | **type**             | the type of the sensor on the virtual joystick to update.             |
| [Uint64](Uint64)                 | **sensor_timestamp** | a 64-bit timestamp in nanoseconds associated with the sensor reading. |
| const float *                    | **data**             | the data associated with the sensor reading.                          |
| int                              | **num_values**       | the number of values pointed to by `data`.                            |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Please note that values set here will not be applied until the next call to
[SDL_UpdateJoysticks](SDL_UpdateJoysticks), which can either be called
directly, or can be called indirectly through various other SDL APIs,
including, but not limited to the following:
[SDL_PollEvent](SDL_PollEvent), [SDL_PumpEvents](SDL_PumpEvents),
[SDL_WaitEventTimeout](SDL_WaitEventTimeout),
[SDL_WaitEvent](SDL_WaitEvent).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetJoystickVirtualAxis](SDL_SetJoystickVirtualAxis)
- [SDL_SetJoystickVirtualButton](SDL_SetJoystickVirtualButton)
- [SDL_SetJoystickVirtualBall](SDL_SetJoystickVirtualBall)
- [SDL_SetJoystickVirtualHat](SDL_SetJoystickVirtualHat)
- [SDL_SetJoystickVirtualTouchpad](SDL_SetJoystickVirtualTouchpad)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

