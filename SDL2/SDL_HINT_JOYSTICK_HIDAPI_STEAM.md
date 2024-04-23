###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_JOYSTICK_HIDAPI_STEAM

A variable controlling whether the HIDAPI driver for Bluetooth Steam Controllers should be used.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_STEAM "SDL_JOYSTICK_HIDAPI_STEAM"
```

## Remarks

This variable can be set to the following values:

- "0": HIDAPI driver is not used
- "1": HIDAPI driver is used for Steam Controllers, which requires
  Bluetooth access and may prompt the user for permission on iOS and
  Android.

The default is "0"

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

