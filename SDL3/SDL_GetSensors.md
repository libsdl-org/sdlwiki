# SDL_GetSensors

Get a list of currently connected sensors.

## Header File

Defined in [<SDL3/SDL_sensor.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_sensor.h)

## Syntax

```c
SDL_SensorID * SDL_GetSensors(int *count);
```

## Function Parameters

|       |           |                                                                       |
| ----- | --------- | --------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of sensors returned, may be NULL. |

## Return Value

([SDL_SensorID](SDL_SensorID) *) Returns a 0 terminated array of sensor
instance IDs or NULL on failure; call [SDL_GetError](SDL_GetError)() for
more information. This should be freed with [SDL_free](SDL_free)() when it
is no longer needed.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

