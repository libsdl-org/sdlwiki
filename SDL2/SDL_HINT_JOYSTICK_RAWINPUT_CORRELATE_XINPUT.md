###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_JOYSTICK_RAWINPUT_CORRELATE_XINPUT

A variable controlling whether the RAWINPUT driver should pull correlated data from XInput.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_RAWINPUT_CORRELATE_XINPUT   "SDL_JOYSTICK_RAWINPUT_CORRELATE_XINPUT"
```

## Remarks

This variable can be set to the following values:

- "0": RAWINPUT driver will only use data from raw input APIs
- "1": RAWINPUT driver will also pull data from XInput, providing better
  trigger axes, guide button presses, and rumble support for Xbox
  controllers

The default is "1". This hint applies to any joysticks opened after setting
the hint.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

