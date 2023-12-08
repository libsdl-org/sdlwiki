###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorGetType

Get the type of a sensor.

## Syntax

```c
SDL_SensorType SDL_SensorGetType(SDL_Sensor *sensor);

```

## Function Parameters

|                |                                                |
| -------------- | ---------------------------------------------- |
| **sensor**     | The [SDL_Sensor](SDL_Sensor.md) object to inspect |

## Return Value

Returns the [SDL_SensorType](SDL_SensorType.md) type, or
[`SDL_SENSOR_INVALID`](SDL_SENSOR_INVALID) if `sensor` is NULL.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI.md)
