###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorGetDeviceName

Get the implementation dependent name of a sensor.

## Syntax

```c
const char* SDL_SensorGetDeviceName(int device_index);

```

## Function Parameters

|                      |                                |
| -------------------- | ------------------------------ |
| **device_index**     | The sensor to obtain name from |

## Return Value

Returns the sensor name, or NULL if `device_index` is out of range.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI.md)
