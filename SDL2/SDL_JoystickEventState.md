###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickEventState

Enable/disable joystick event polling.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
int SDL_JoystickEventState(int state);

```

## Function Parameters

|               |                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------- |
| **state**     | can be one of [`SDL_QUERY`](SDL_QUERY), [`SDL_IGNORE`](SDL_IGNORE), or [`SDL_ENABLE`](SDL_ENABLE) |

## Return Value

Returns If `state` is [`SDL_QUERY`](SDL_QUERY) then the current state is
returned, otherwise `state` is returned (even if it was not one of the
allowed values).

## Remarks

If joystick events are disabled, you must call
[SDL_JoystickUpdate](SDL_JoystickUpdate)() yourself and manually check the
state of the joystick when you want joystick information.

It is recommended that you leave joystick event handling enabled.

**WARNING**: Calling this function may delete all events currently in SDL's
event queue.

While `param` is meant to be one of [`SDL_QUERY`](SDL_QUERY),
[`SDL_IGNORE`](SDL_IGNORE), or [`SDL_ENABLE`](SDL_ENABLE), this function
accepts any value, with any non-zero value that isn't
[`SDL_QUERY`](SDL_QUERY) being treated as [`SDL_ENABLE`](SDL_ENABLE).

If SDL was built with events disabled (extremely uncommon!), this will do
nothing and always return [`SDL_IGNORE`](SDL_IGNORE).

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GameControllerEventState](SDL_GameControllerEventState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

