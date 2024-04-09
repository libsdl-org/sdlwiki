###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_STANDARD_GRAVITY

Accelerometer sensor.

## Header File

Defined in [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_sensor.h), but apps should _only_ `#include <SDL3/SDL.h>`!

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

For phones and tablets held in natural orientation and game controllers
held in front of you, the axes are defined as follows:

- -X ... +X : left ... right
- -Y ... +Y : bottom ... top
- -Z ... +Z : farther ... closer

The axis data is not changed when the device is rotated.

## See Also

* [SDL_GetCurrentDisplayOrientation](SDL_GetCurrentDisplayOrientation)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

