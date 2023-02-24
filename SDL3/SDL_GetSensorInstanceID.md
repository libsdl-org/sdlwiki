###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSensorInstanceID

Get the instance ID of a sensor.

## Syntax

```c
SDL_SensorID SDL_GetSensorInstanceID(SDL_Sensor *sensor);

```

## Function Parameters

|                |                                                |
| -------------- | ---------------------------------------------- |
| **sensor**     | The [SDL_Sensor](SDL_Sensor) object to inspect |

## Return Value

Returns the sensor instance ID, or 0 if `sensor` is NULL.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

