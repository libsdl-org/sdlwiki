###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
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

Return [SDL_TRUE](SDL_TRUE.md) if the joystick has rumble,
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Version

This function is available since SDL 2.0.18.

## Related Functions

* [SDL_JoystickRumble](SDL_JoystickRumble.md)

----
[CategoryAPI](CategoryAPI.md)
