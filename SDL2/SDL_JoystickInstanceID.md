###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickInstanceID

Get the instance ID of an opened joystick.

## Syntax

```c
SDL_JoystickID SDL_JoystickInstanceID(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                           |
| ---------------- | ------------------------------------------------------------------------- |
| **joystick**     | an [SDL_Joystick](SDL_Joystick.md) structure containing joystick information |

## Return Value

Returns the instance ID of the specified joystick on success or a negative
error code on failure; call [SDL_GetError](SDL_GetError.md)() for more
information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_JoystickOpen](SDL_JoystickOpen.md)

----
[CategoryAPI](CategoryAPI.md)
