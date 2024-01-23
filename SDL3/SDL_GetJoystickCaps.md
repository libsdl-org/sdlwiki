###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickCaps

Query joystick capabilities 

## Syntax

```c
Uint32 SDL_GetJoystickCaps(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **joystick**     | The joystick to query |

## Return Value

Returns a mask of [SDL_JoystickCaps](SDL_JoystickCaps) values indicating
the joystick capabilities.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

