# SDL_OpenSensor

Open a sensor for use.

## Header File

Defined in [<SDL3/SDL_sensor.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_sensor.h)

## Syntax

```c
SDL_Sensor * SDL_OpenSensor(SDL_SensorID instance_id);
```

## Function Parameters

|                              |                 |                         |
| ---------------------------- | --------------- | ----------------------- |
| [SDL_SensorID](SDL_SensorID) | **instance_id** | the sensor instance ID. |

## Return Value

([SDL_Sensor](SDL_Sensor) *) Returns an [SDL_Sensor](SDL_Sensor) object or
NULL on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

