###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_JOYSTICK_HIDAPI_PS3

A variable controlling whether the HIDAPI driver for PS3 controllers should be used.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_PS3 "SDL_JOYSTICK_HIDAPI_PS3"
```

## Remarks

The variable can be set to the following values:

- "0": HIDAPI driver is not used.
- "1": HIDAPI driver is used.

The default is the value of
[SDL_HINT_JOYSTICK_HIDAPI](SDL_HINT_JOYSTICK_HIDAPI) on macOS, and "0" on
other platforms.

For official Sony driver (sixaxis.sys) use
[SDL_HINT_JOYSTICK_HIDAPI_PS3_SIXAXIS_DRIVER](SDL_HINT_JOYSTICK_HIDAPI_PS3_SIXAXIS_DRIVER).
See https://github.com/ViGEm/DsHidMini for an alternative driver on
Windows.

This hint should be set before enumerating controllers.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

