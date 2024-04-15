###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSensorName

Get the implementation dependent name of a sensor.

## Header File

Defined in [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_sensor.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
const char* SDL_GetSensorName(SDL_Sensor *sensor);

```

## Function Parameters

|                |                                     |
| -------------- | ----------------------------------- |
| **sensor**     | The [SDL_Sensor](SDL_Sensor) object |

## Return Value

Returns the sensor name, or NULL if `sensor` is NULL.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

