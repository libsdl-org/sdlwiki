###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadSensorData

Get the current state of a gamepad sensor.

## Syntax

```c
int SDL_GetGamepadSensorData(SDL_Gamepad *gamepad, SDL_SensorType type, float *data, int num_values);

```

## Function Parameters

|                    |                                                |
| ------------------ | ---------------------------------------------- |
| **gamepad**        | The gamepad to query                           |
| **type**           | The type of sensor to query                    |
| **data**           | A pointer filled with the current sensor state |
| **num_values**     | The number of values to write to data          |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The number of values and interpretation of the data is sensor dependent.
See [SDL_sensor](SDL_sensor).h for the details for each type of sensor.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

