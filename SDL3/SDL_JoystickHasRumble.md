###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_JoystickHasRumble

Query whether a joystick has rumble support.

## Syntax

```c
SDL_bool SDL_JoystickHasRumble(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **joystick**     | The joystick to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the joystick has rumble,
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_RumbleJoystick](SDL_RumbleJoystick.md)

----
[CategoryAPI](CategoryAPI.md)
