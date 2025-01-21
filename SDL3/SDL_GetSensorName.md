###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetSensorName

Get the implementation dependent name of a sensor.

## Header File

Defined in [<SDL3/SDL_sensor.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_sensor.h)

## Syntax

```c
const char * SDL_GetSensorName(SDL_Sensor *sensor);
```

## Function Parameters

|                            |            |                                      |
| -------------------------- | ---------- | ------------------------------------ |
| [SDL_Sensor](SDL_Sensor) * | **sensor** | the [SDL_Sensor](SDL_Sensor) object. |

## Return Value

(const char *) Returns the sensor name or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

