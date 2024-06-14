###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorOpen

Open a sensor for use.

## Header File

Defined in [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_sensor.h)

## Syntax

```c
SDL_Sensor* SDL_SensorOpen(int device_index);
```

## Function Parameters

|     |                  |                     |
| --- | ---------------- | ------------------- |
| int | **device_index** | The sensor to open. |

## Return Value

([SDL_Sensor](SDL_Sensor) *) Returns an [SDL_Sensor](SDL_Sensor) sensor
object, or NULL if an error occurred.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

