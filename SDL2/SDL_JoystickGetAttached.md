###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetAttached

Get the status of a specified joystick.

## Syntax

```c
SDL_bool SDL_JoystickGetAttached(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **joystick**     | the joystick to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the joystick has been opened,
[SDL_FALSE](SDL_FALSE.md) if it has not; call [SDL_GetError](SDL_GetError.md)()
for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_JoystickClose](SDL_JoystickClose.md)
* [SDL_JoystickOpen](SDL_JoystickOpen.md)

----
[CategoryAPI](CategoryAPI.md)
