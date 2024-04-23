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

This variable can be set to the following values: "0" - The accelerometer
is not listed as a joystick "1" - The accelerometer is available as a 3
axis joystick (the default).

## Code Examples

```c++
#include "SDL.h"

int main(int argc, char* argv[])
{
    // This disables the use of gyroscopes as axis device
    SDL_SetHint(SDL_HINT_ACCELEROMETER_AS_JOYSTICK, "0");
}

```

## Default

By default SDL will list real joysticks along with the accelerometer as if it were a 3 axis joystick.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints)
<!-- #See the Style Guide for instructions on editing the footer. -->


