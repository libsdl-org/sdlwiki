# SDL_GetSensorID

Get the instance ID of a sensor.

## Header File

Defined in [<SDL3/SDL_sensor.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_sensor.h)

## Syntax

```c
SDL_SensorID SDL_GetSensorID(SDL_Sensor *sensor);
```

## Function Parameters

|                            |            |                                                 |
| -------------------------- | ---------- | ----------------------------------------------- |
| [SDL_Sensor](SDL_Sensor) * | **sensor** | the [SDL_Sensor](SDL_Sensor) object to inspect. |

## Return Value

([SDL_SensorID](SDL_SensorID)) Returns the sensor instance ID, or 0 on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

