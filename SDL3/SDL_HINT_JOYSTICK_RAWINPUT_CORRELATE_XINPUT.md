###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_JOYSTICK_RAWINPUT_CORRELATE_XINPUT

A variable controlling whether the RAWINPUT driver should pull correlated data from XInput.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_RAWINPUT_CORRELATE_XINPUT   "SDL_JOYSTICK_RAWINPUT_CORRELATE_XINPUT"
```

## Remarks

The variable can be set to the following values:

- "0": RAWINPUT driver will only use data from raw input APIs.
- "1": RAWINPUT driver will also pull data from XInput and
  Windows.Gaming.Input, providing better trigger axes, guide button
  presses, and rumble support for Xbox controllers. (default)

This hint should be set before a gamepad is opened.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

