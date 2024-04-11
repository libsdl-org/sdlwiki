###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_JOYSTICK_HIDAPI_XBOX_360_WIRELESS

A variable controlling whether the HIDAPI driver for XBox 360 wireless controllers should be used.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_XBOX_360_WIRELESS   "SDL_JOYSTICK_HIDAPI_XBOX_360_WIRELESS"
```

## Remarks

This variable can be set to the following values: "0" - HIDAPI driver is
not used "1" - HIDAPI driver is used

The default is the value of
[SDL_HINT_JOYSTICK_HIDAPI_XBOX_360](SDL_HINT_JOYSTICK_HIDAPI_XBOX_360)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

