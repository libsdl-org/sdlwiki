###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_JOYSTICK_HIDAPI_PS4_RUMBLE

A variable controlling whether extended input reports should be used for PS4 controllers when using the HIDAPI driver.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_PS4_RUMBLE "SDL_JOYSTICK_HIDAPI_PS4_RUMBLE"
```

## Remarks

The variable can be set to the following values:

- "0": extended reports are not enabled. (default)
- "1": extended reports are enabled.

Extended input reports allow rumble on Bluetooth PS4 controllers, but break
DirectInput handling for applications that don't use SDL.

Once extended reports are enabled, they can not be disabled without power
cycling the controller.

For compatibility with applications written for versions of SDL prior to
the introduction of PS5 controller support, this value will also control
the state of extended reports on PS5 controllers when the
[SDL_HINT_JOYSTICK_HIDAPI_PS5_RUMBLE](SDL_HINT_JOYSTICK_HIDAPI_PS5_RUMBLE)
hint is not explicitly set.

This hint can be enabled anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

