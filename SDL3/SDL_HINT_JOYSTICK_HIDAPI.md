# SDL_HINT_JOYSTICK_HIDAPI

A variable controlling whether the HIDAPI joystick drivers should be used.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI "SDL_JOYSTICK_HIDAPI"
```

## Remarks

The variable can be set to the following values:

- "0": HIDAPI drivers are not used.
- "1": HIDAPI drivers are used. (default)

This variable is the default for all drivers, but can be overridden by the
hints for specific drivers below.

This hint should be set before initializing joysticks and gamepads.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

