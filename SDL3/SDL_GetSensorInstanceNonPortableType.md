###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSensorInstanceNonPortableType

Get the platform dependent type of a sensor.

## Header File

Defined in [<SDL3/SDL_sensor.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_sensor.h)

## Syntax

```c
int SDL_GetSensorInstanceNonPortableType(SDL_SensorID instance_id);
```

## Function Parameters

|                              |                 |                        |
| ---------------------------- | --------------- | ---------------------- |
| [SDL_SensorID](SDL_SensorID) | **instance_id** | the sensor instance ID |

## Return Value

(int) Returns the sensor platform dependent type, or -1 if `instance_id` is
not valid

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

