###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GamepadAxis

The list of axes available on a gamepad

## Header File

Defined in [SDL_gamepad.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef enum SDL_GamepadAxis
{
    SDL_GAMEPAD_AXIS_INVALID = -1,
    SDL_GAMEPAD_AXIS_LEFTX,
    SDL_GAMEPAD_AXIS_LEFTY,
    SDL_GAMEPAD_AXIS_RIGHTX,
    SDL_GAMEPAD_AXIS_RIGHTY,
    SDL_GAMEPAD_AXIS_LEFT_TRIGGER,
    SDL_GAMEPAD_AXIS_RIGHT_TRIGGER,
    SDL_GAMEPAD_AXIS_MAX
} SDL_GamepadAxis;
```

## Remarks

Thumbstick axis values range from
[SDL_JOYSTICK_AXIS_MIN](SDL_JOYSTICK_AXIS_MIN) to
[SDL_JOYSTICK_AXIS_MAX](SDL_JOYSTICK_AXIS_MAX), and are centered within
~8000 of zero, though advanced UI will allow users to set or autodetect the
dead zone, which varies between gamepads.

Trigger axis values range from 0 (released) to
[SDL_JOYSTICK_AXIS_MAX](SDL_JOYSTICK_AXIS_MAX) (fully pressed) when
reported by [SDL_GetGamepadAxis](SDL_GetGamepadAxis)(). Note that this is
not the same range that will be reported by the lower-level
[SDL_GetJoystickAxis](SDL_GetJoystickAxis)().

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

