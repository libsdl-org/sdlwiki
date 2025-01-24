# SDL_GetSensorNameForID

Get the implementation dependent name of a sensor.

## Header File

Defined in [<SDL3/SDL_sensor.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_sensor.h)

## Syntax

```c
const char * SDL_GetSensorNameForID(SDL_SensorID instance_id);
```

## Function Parameters

|                              |                 |                         |
| ---------------------------- | --------------- | ----------------------- |
| [SDL_SensorID](SDL_SensorID) | **instance_id** | the sensor instance ID. |

## Return Value

(const char *) Returns the sensor name, or NULL if `instance_id` is not
valid.

## Remarks

This can be called before any sensors are opened.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

