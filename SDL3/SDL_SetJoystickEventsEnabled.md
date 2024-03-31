###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetJoystickEventsEnabled

Set the state of joystick event processing.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
void SDL_SetJoystickEventsEnabled(SDL_bool enabled);

```

## Function Parameters

|                 |                                           |
| --------------- | ----------------------------------------- |
| **enabled**     | whether to process joystick events or not |

## Remarks

If joystick events are disabled, you must call
[SDL_UpdateJoysticks](SDL_UpdateJoysticks)() yourself and check the state
of the joystick when you want joystick information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_JoystickEventsEnabled](SDL_JoystickEventsEnabled)
* [SDL_UpdateJoysticks](SDL_UpdateJoysticks)

----
[CategoryAPI](CategoryAPI)

