# SDL_HINT_JOYSTICK_HIDAPI_XBOX_360_WIRELESS

A variable controlling whether the HIDAPI driver for XBox 360 wireless controllers should be used.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_XBOX_360_WIRELESS "SDL_JOYSTICK_HIDAPI_XBOX_360_WIRELESS"
```

## Remarks

The variable can be set to the following values:

- "0": HIDAPI driver is not used.
- "1": HIDAPI driver is used.

The default is the value of
[SDL_HINT_JOYSTICK_HIDAPI_XBOX_360](SDL_HINT_JOYSTICK_HIDAPI_XBOX_360)

This hint should be set before initializing joysticks and gamepads.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

