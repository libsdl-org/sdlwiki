###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSensorType

Get the type of a sensor.

## Syntax

```c
SDL_SensorType SDL_GetSensorType(SDL_Sensor *sensor);

```

## Function Parameters

|                |                                                |
| -------------- | ---------------------------------------------- |
| **sensor**     | The [SDL_Sensor](SDL_Sensor) object to inspect |

## Return Value

Returns the [SDL_SensorType](SDL_SensorType) type, or
[`SDL_SENSOR_INVALID`](SDL_SENSOR_INVALID) if `sensor` is NULL.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

