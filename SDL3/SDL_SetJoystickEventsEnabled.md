# SDL_SetJoystickEventsEnabled

Set the state of joystick event processing.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
void SDL_SetJoystickEventsEnabled(bool enabled);
```

## Function Parameters

|      |             |                                            |
| ---- | ----------- | ------------------------------------------ |
| bool | **enabled** | whether to process joystick events or not. |

## Remarks

If joystick events are disabled, you must call
[SDL_UpdateJoysticks](SDL_UpdateJoysticks)() yourself and check the state
of the joystick when you want joystick information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_JoystickEventsEnabled](SDL_JoystickEventsEnabled)
- [SDL_UpdateJoysticks](SDL_UpdateJoysticks)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

