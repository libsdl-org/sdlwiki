# SDL_SensorGetNonPortableType

Get the platform dependent type of a sensor.

## Header File

Defined in [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_sensor.h)

## Syntax

```c
int SDL_SensorGetNonPortableType(SDL_Sensor *sensor);
```

## Function Parameters

|                            |            |                                                 |
| -------------------------- | ---------- | ----------------------------------------------- |
| [SDL_Sensor](SDL_Sensor) * | **sensor** | The [SDL_Sensor](SDL_Sensor) object to inspect. |

## Return Value

(int) Returns the sensor platform dependent type, or -1 if `sensor` is
NULL.

## Version

This function is available since SDL 2.0.9.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

