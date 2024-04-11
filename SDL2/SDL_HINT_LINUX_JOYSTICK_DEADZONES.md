###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_LINUX_JOYSTICK_DEADZONES

A variable controlling whether joysticks on Linux adhere to their HID-defined deadzones or return unfiltered values.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_LINUX_JOYSTICK_DEADZONES "SDL_LINUX_JOYSTICK_DEADZONES"
```

## Remarks

This variable can be set to the following values: "0" - Return unfiltered
joystick axis values (the default) "1" - Return axis values with deadzones
taken into account

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

