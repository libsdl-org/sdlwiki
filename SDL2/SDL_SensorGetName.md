###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorGetName

Get the implementation dependent name of a sensor

## Header File

Defined in [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_sensor.h)

## Syntax

```c
const char* SDL_SensorGetName(SDL_Sensor *sensor);

```

## Function Parameters

|                |                                     |
| -------------- | ----------------------------------- |
| **sensor**     | The [SDL_Sensor](SDL_Sensor) object |

## Return Value

Returns the sensor name, or NULL if `sensor` is NULL.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

