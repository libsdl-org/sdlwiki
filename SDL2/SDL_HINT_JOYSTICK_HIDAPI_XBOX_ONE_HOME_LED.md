# SDL_HINT_JOYSTICK_HIDAPI_XBOX_ONE_HOME_LED

A variable controlling whether the Home button LED should be turned on when an Xbox One controller is opened

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_XBOX_ONE_HOME_LED "SDL_JOYSTICK_HIDAPI_XBOX_ONE_HOME_LED"
```

## Remarks

This variable can be set to the following values:

- "0": home button LED is turned off
- "1": home button LED is turned on

By default the Home button LED state is not changed. This hint can also be
set to a floating point value between 0.0 and 1.0 which controls the
brightness of the Home button LED. The default brightness is 0.4.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

