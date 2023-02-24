###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetNumJoystickHats

Get the number of POV hats on a joystick.

## Syntax

```c
int SDL_GetNumJoystickHats(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                           |
| ---------------- | ------------------------------------------------------------------------- |
| **joystick**     | an [SDL_Joystick](SDL_Joystick) structure containing joystick information |

## Return Value

Returns the number of POV hats on success or a negative error code on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetJoystickHat](SDL_GetJoystickHat)
* [SDL_OpenJoystick](SDL_OpenJoystick)

----
[CategoryAPI](CategoryAPI)

