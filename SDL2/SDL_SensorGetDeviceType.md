###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorGetDeviceType

Get the type of a sensor.

## Header File

Defined in [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_sensor.h)

## Syntax

```c
SDL_SensorType SDL_SensorGetDeviceType(int device_index);
```

## Function Parameters

|     |                  |                                  |
| --- | ---------------- | -------------------------------- |
| int | **device_index** | The sensor to get the type from. |

## Return Value

([SDL_SensorType](SDL_SensorType)) Returns the
[SDL_SensorType](SDL_SensorType), or
[`SDL_SENSOR_INVALID`](SDL_SENSOR_INVALID) if `device_index` is out of
range.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

