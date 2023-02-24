###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickEventState

Enable/disable joystick event polling.

## Syntax

```c
int SDL_JoystickEventState(int state);

```

## Function Parameters

|               |                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------- |
| **state**     | can be one of [`SDL_QUERY`](SDL_QUERY), [`SDL_IGNORE`](SDL_IGNORE), or [`SDL_ENABLE`](SDL_ENABLE) |

## Return Value

Returns 1 if enabled, 0 if disabled, or a negative error code on failure;
call [SDL_GetError](SDL_GetError)() for more information.

If `state` is [`SDL_QUERY`](SDL_QUERY) then the current state is returned,
otherwise the new processing state is returned.

## Remarks

If joystick events are disabled, you must call
[SDL_JoystickUpdate](SDL_JoystickUpdate)() yourself and manually check the
state of the joystick when you want joystick information.

It is recommended that you leave joystick event handling enabled.

**WARNING**: Calling this function may delete all events currently in SDL's
event queue.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GameControllerEventState](SDL_GameControllerEventState)

----
[CategoryAPI](CategoryAPI)

