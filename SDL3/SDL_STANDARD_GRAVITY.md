###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_STANDARD_GRAVITY

A constant to represent standard gravity for accelerometer sensors.

## Header File

Defined in [<SDL3/SDL_sensor.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_sensor.h)

## Syntax

```c
#define SDL_STANDARD_GRAVITY    9.80665f
```

## Remarks

The accelerometer returns the current acceleration in SI meters per second
squared. This measurement includes the force of gravity, so a device at
rest will have an value of [SDL_STANDARD_GRAVITY](SDL_STANDARD_GRAVITY)
away from the center of the earth, which is a positive Y value.

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategorySensor](CategorySensor)

