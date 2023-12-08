###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorGetData

Get the current state of an opened sensor.

## Syntax

```c
int SDL_SensorGetData(SDL_Sensor *sensor, float *data, int num_values);

```

## Function Parameters

|                    |                                                |
| ------------------ | ---------------------------------------------- |
| **sensor**         | The [SDL_Sensor](SDL_Sensor.md) object to query   |
| **data**           | A pointer filled with the current sensor state |
| **num_values**     | The number of values to write to data          |

## Return Value

Returns 0 or -1 if an error occurred.

## Remarks

The number of values and interpretation of the data is sensor dependent.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI.md)
