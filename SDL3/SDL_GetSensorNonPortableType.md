###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSensorNonPortableType

Get the platform dependent type of a sensor.

## Syntax

```c
int SDL_GetSensorNonPortableType(SDL_Sensor *sensor);

```

## Function Parameters

|                |                                                |
| -------------- | ---------------------------------------------- |
| **sensor**     | The [SDL_Sensor](SDL_Sensor) object to inspect |

## Return Value

Returns the sensor platform dependent type, or -1 if `sensor` is NULL.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

