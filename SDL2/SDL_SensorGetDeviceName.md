###### (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)
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

## (This is the legacy documentation for stable SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)



## (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

