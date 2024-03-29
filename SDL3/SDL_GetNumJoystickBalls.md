###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetNumJoystickBalls

Get the number of trackballs on a joystick.

## Syntax

```c
int SDL_GetNumJoystickBalls(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                           |
| ---------------- | ------------------------------------------------------------------------- |
| **joystick**     | an [SDL_Joystick](SDL_Joystick) structure containing joystick information |

## Return Value

Returns the number of trackballs on success or a negative error code on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Joystick trackballs have only relative motion events associated with them
and their state cannot be polled.

Most joysticks do not have trackballs.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetJoystickBall](SDL_GetJoystickBall)
* [SDL_GetNumJoystickAxes](SDL_GetNumJoystickAxes)
* [SDL_GetNumJoystickButtons](SDL_GetNumJoystickButtons)
* [SDL_GetNumJoystickHats](SDL_GetNumJoystickHats)

----
[CategoryAPI](CategoryAPI)

