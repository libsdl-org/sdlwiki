###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_JOYSTICK_HIDAPI_PS3

A variable controlling whether the HIDAPI driver for PS3 controllers should be used.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_PS3 "SDL_JOYSTICK_HIDAPI_PS3"
```

## Remarks

This variable can be set to the following values: "0" - HIDAPI driver is
not used "1" - HIDAPI driver is used

The default is the value of
[SDL_HINT_JOYSTICK_HIDAPI](SDL_HINT_JOYSTICK_HIDAPI) on macOS, and "0" on
other platforms.

It is not possible to use this driver on Windows, due to limitations in the
default drivers installed. See https://github.com/ViGEm/DsHidMini for an
alternative driver on Windows.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

