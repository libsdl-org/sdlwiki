###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorOpen

Open a sensor for use.

## Syntax

```c
SDL_Sensor* SDL_SensorOpen(int device_index);

```

## Function Parameters

|                      |                    |
| -------------------- | ------------------ |
| **device_index**     | The sensor to open |

## Return Value

Returns an [SDL_Sensor](SDL_Sensor.md) sensor object, or NULL if an error
occurred.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI.md)
