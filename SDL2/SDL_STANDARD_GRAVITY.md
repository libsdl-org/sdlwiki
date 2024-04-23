###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_STANDARD_GRAVITY

Accelerometer sensor

## Header File

Defined in [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_sensor.h)

## Syntax

```c
#define SDL_STANDARD_GRAVITY    9.80665f
```

## Remarks

The accelerometer returns the current acceleration in SI meters per second
squared. This measurement includes the force of gravity, so a device at
rest will have an value of [SDL_STANDARD_GRAVITY](SDL_STANDARD_GRAVITY)
away from the center of the earth, which is a positive Y value.

values[0]: Acceleration on the x axis values[1]: Acceleration on the y axis
values[2]: Acceleration on the z axis

For phones held in portrait mode and game controllers held in front of you,
the axes are defined as follows: -X ... +X : left ... right -Y ... +Y :
bottom ... top -Z ... +Z : farther ... closer

The axis data is not changed when the phone is rotated.

## Related Functions

* [SDL_GetDisplayOrientation](SDL_GetDisplayOrientation)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

