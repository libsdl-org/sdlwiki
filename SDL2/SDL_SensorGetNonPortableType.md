###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorGetNonPortableType

Get the platform dependent type of a sensor.

## Syntax

```c
int SDL_SensorGetNonPortableType(SDL_Sensor *sensor);

```

## Function Parameters

|                |                                                |
| -------------- | ---------------------------------------------- |
| **sensor**     | The [SDL_Sensor](SDL_Sensor.md) object to inspect |

## Return Value

Returns the sensor platform dependent type, or -1 if `sensor` is NULL.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI.md)
