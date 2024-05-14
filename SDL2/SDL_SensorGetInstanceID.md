###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorGetInstanceID

Get the instance ID of a sensor.

## Header File

Defined in [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_sensor.h)

## Syntax

```c
SDL_SensorID SDL_SensorGetInstanceID(SDL_Sensor *sensor);

```

## Function Parameters

|                |                                                |
| -------------- | ---------------------------------------------- |
| **sensor**     | The [SDL_Sensor](SDL_Sensor) object to inspect |

## Return Value

Returns the sensor instance ID, or -1 if `sensor` is NULL.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

