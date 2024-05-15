###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerAxis

The list of axes available from a controller

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
typedef enum SDL_GameControllerAxis
{
    SDL_CONTROLLER_AXIS_INVALID = -1,
    SDL_CONTROLLER_AXIS_LEFTX,
    SDL_CONTROLLER_AXIS_LEFTY,
    SDL_CONTROLLER_AXIS_RIGHTX,
    SDL_CONTROLLER_AXIS_RIGHTY,
    SDL_CONTROLLER_AXIS_TRIGGERLEFT,
    SDL_CONTROLLER_AXIS_TRIGGERRIGHT,
    SDL_CONTROLLER_AXIS_MAX
} SDL_GameControllerAxis;
```

## Remarks

Thumbstick axis values range from
[SDL_JOYSTICK_AXIS_MIN](SDL_JOYSTICK_AXIS_MIN) to
[SDL_JOYSTICK_AXIS_MAX](SDL_JOYSTICK_AXIS_MAX), and are centered within
~8000 of zero, though advanced UI will allow users to set or autodetect the
dead zone, which varies between controllers.

Trigger axis values range from 0 (released) to
[SDL_JOYSTICK_AXIS_MAX](SDL_JOYSTICK_AXIS_MAX) (fully pressed) when
reported by [SDL_GameControllerGetAxis](SDL_GameControllerGetAxis)(). Note
that this is not the same range that will be reported by the lower-level
[SDL_GetJoystickAxis](SDL_GetJoystickAxis)().

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGameController](CategoryGameController)

