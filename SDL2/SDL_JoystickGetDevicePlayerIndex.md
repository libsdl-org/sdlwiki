###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetDevicePlayerIndex

Get the player index of a joystick, or -1 if it's not available This can be called before any joysticks are opened.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_JoystickGetDevicePlayerIndex(int device_index);

```

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI)

