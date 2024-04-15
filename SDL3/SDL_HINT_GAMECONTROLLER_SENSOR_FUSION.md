###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_GAMECONTROLLER_SENSOR_FUSION

A variable that controls whether the device's built-in accelerometer and gyro should be used as sensors for gamepads.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_GAMECONTROLLER_SENSOR_FUSION "SDL_GAMECONTROLLER_SENSOR_FUSION"
```

## Remarks

The variable can be set to the following values:

- "0": Sensor fusion is disabled
- "1": Sensor fusion is enabled for all controllers that lack sensors

Or the variable can be a comma separated list of USB VID/PID pairs in
hexadecimal form, e.g.

0xAAAA/0xBBBB,0xCCCC/0xDDDD

The variable can also take the form of "@file", in which case the named
file will be loaded and interpreted as the value of the variable.

This hint should be set before a gamepad is opened.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

