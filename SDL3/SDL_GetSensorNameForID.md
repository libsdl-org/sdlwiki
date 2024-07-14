###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSensorNameForID

Get the implementation dependent name of a sensor.

## Header File

Defined in [<SDL3/SDL_sensor.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_sensor.h)

## Syntax

```c
const char* SDL_GetSensorNameForID(SDL_SensorID instance_id);
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

The returned string follows the [SDL_GetStringRule](SDL_GetStringRule).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

