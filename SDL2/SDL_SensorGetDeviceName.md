# SDL_SensorGetDeviceName

Get the implementation dependent name of a sensor.

## Header File

Defined in [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_sensor.h)

## Syntax

```c
const char* SDL_SensorGetDeviceName(int device_index);
```

## Function Parameters

|     |                  |                                 |
| --- | ---------------- | ------------------------------- |
| int | **device_index** | The sensor to obtain name from. |

## Return Value

(const char *) Returns the sensor name, or NULL if `device_index` is out of
range.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

