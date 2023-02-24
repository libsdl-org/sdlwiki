###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSensorData

Get the current state of an opened sensor.

## Syntax

```c
int SDL_GetSensorData(SDL_Sensor *sensor, float *data, int num_values);

```

## Function Parameters

|                    |                                                |
| ------------------ | ---------------------------------------------- |
| **sensor**         | The [SDL_Sensor](SDL_Sensor) object to query   |
| **data**           | A pointer filled with the current sensor state |
| **num_values**     | The number of values to write to data          |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The number of values and interpretation of the data is sensor dependent.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

