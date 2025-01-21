###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_JOYSTICK_HIDAPI_STEAM_HOME_LED

A variable controlling whether the Steam button LED should be turned on when a Steam controller is opened.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_STEAM_HOME_LED "SDL_JOYSTICK_HIDAPI_STEAM_HOME_LED"
```

## Remarks

The variable can be set to the following values:

- "0": Steam button LED is turned off.
- "1": Steam button LED is turned on.

By default the Steam button LED state is not changed. This hint can also be
set to a floating point value between 0.0 and 1.0 which controls the
brightness of the Steam button LED.

This hint can be set anytime.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

