# SDL_GetGamepadSensorData

Get the current state of a gamepad sensor.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
bool SDL_GetGamepadSensorData(SDL_Gamepad *gamepad, SDL_SensorType type, float *data, int num_values);
```

## Function Parameters

|                                  |                |                                                 |
| -------------------------------- | -------------- | ----------------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) *     | **gamepad**    | the gamepad to query.                           |
| [SDL_SensorType](SDL_SensorType) | **type**       | the type of sensor to query.                    |
| float *                          | **data**       | a pointer filled with the current sensor state. |
| int                              | **num_values** | the number of values to write to data.          |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The number of values and interpretation of the data is sensor dependent.
See [SDL_sensor](SDL_sensor).h for the details for each type of sensor.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

