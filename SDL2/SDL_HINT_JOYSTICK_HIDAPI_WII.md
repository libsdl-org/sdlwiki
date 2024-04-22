###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_JOYSTICK_HIDAPI_WII

A variable controlling whether the HIDAPI driver for Nintendo Wii and Wii U controllers should be used.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_WII "SDL_JOYSTICK_HIDAPI_WII"
```

## Remarks

This variable can be set to the following values: "0" - HIDAPI driver is
not used "1" - HIDAPI driver is used

This driver doesn't work with the dolphinbar, so the default is
[SDL_FALSE](SDL_FALSE) for now.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

