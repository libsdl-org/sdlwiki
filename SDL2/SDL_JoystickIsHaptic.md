###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickIsHaptic

Query if a joystick has haptic features.

## Syntax

```c
int SDL_JoystickIsHaptic(SDL_Joystick * joystick);

```

## Function Parameters

|                  |                                                                  |
| ---------------- | ---------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick.md) to test for haptic capabilities |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the joystick is haptic,
[SDL_FALSE](SDL_FALSE.md) if it isn't, or a negative error code on failure;
call [SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticOpenFromJoystick](SDL_HapticOpenFromJoystick.md)

----
[CategoryAPI](CategoryAPI.md)
