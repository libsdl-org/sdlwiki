# SDL_HINT_JOYSTICK_HIDAPI_WII

A variable controlling whether the HIDAPI driver for Nintendo Wii and Wii U controllers should be used.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_WII "SDL_JOYSTICK_HIDAPI_WII"
```

## Remarks

The variable can be set to the following values:

- "0": HIDAPI driver is not used.
- "1": HIDAPI driver is used.

This driver doesn't work with the dolphinbar, so the default is false for
now.

This hint should be set before initializing joysticks and gamepads.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

