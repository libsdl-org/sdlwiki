###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorGetDeviceType

Get the type of a sensor.

## Syntax

```c
SDL_SensorType SDL_SensorGetDeviceType(int device_index);

```

## Function Parameters

|                      |                                 |
| -------------------- | ------------------------------- |
| **device_index**     | The sensor to get the type from |

## Return Value

Returns the [SDL_SensorType](SDL_SensorType.md), or
[`SDL_SENSOR_INVALID`](SDL_SENSOR_INVALID) if `device_index` is out of
range.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI.md)
