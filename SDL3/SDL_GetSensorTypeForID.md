###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSensorTypeForID

Get the type of a sensor.

## Header File

Defined in [<SDL3/SDL_sensor.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_sensor.h)

## Syntax

```c
SDL_SensorType SDL_GetSensorTypeForID(SDL_SensorID instance_id);
```

## Function Parameters

|                              |                 |                         |
| ---------------------------- | --------------- | ----------------------- |
| [SDL_SensorID](SDL_SensorID) | **instance_id** | the sensor instance ID. |

## Return Value

([SDL_SensorType](SDL_SensorType)) Returns the
[SDL_SensorType](SDL_SensorType), or
[`SDL_SENSOR_INVALID`](SDL_SENSOR_INVALID) if `instance_id` is not valid.

## Remarks

This can be called before any sensors are opened.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

