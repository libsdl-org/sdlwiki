###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_JOYSTICK_HIDAPI_PS4_REPORT_INTERVAL

A variable controlling the update rate of the PS4 controller over Bluetooth when using the HIDAPI driver.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_PS4_REPORT_INTERVAL "SDL_JOYSTICK_HIDAPI_PS4_REPORT_INTERVAL"
```

## Remarks

This defaults to 4 ms, to match the behavior over USB, and to be more
friendly to other Bluetooth devices and older Bluetooth hardware on the
computer. It can be set to "1" (1000Hz), "2" (500Hz) and "4" (250Hz)

This hint can be set anytime, but only takes effect when extended input
reports are enabled.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

