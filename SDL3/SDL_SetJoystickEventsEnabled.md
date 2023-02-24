###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetJoystickEventsEnabled

Set the state of joystick event processing.

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

----
[CategoryAPI](CategoryAPI)

