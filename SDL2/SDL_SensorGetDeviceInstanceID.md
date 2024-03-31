###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorGetDeviceInstanceID

Get the instance ID of a sensor.

## Header File

Defined in [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_sensor.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_SensorID SDL_SensorGetDeviceInstanceID(int device_index);

```

## Function Parameters

|                      |                                    |
| -------------------- | ---------------------------------- |
| **device_index**     | The sensor to get instance id from |

## Return Value

Returns the sensor instance ID, or -1 if `device_index` is out of range.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI)

