###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_ACCELEROMETER_AS_JOYSTICK

A variable controlling whether the Android / iOS built-in accelerometer should be listed as a joystick device.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ACCELEROMETER_AS_JOYSTICK "SDL_ACCELEROMETER_AS_JOYSTICK"
```

## Remarks

This variable can be set to the following values:

- "0": The accelerometer is not listed as a joystick
- "1": The accelerometer is available as a 3 axis joystick (the default).

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints), [CategoryAPIMacro](CategoryAPIMacro), 

