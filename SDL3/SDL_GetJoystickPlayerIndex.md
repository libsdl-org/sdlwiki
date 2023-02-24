###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickPlayerIndex

Get the player index of an opened joystick.

## Syntax

```c
int SDL_GetJoystickPlayerIndex(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_OpenJoystick](SDL_OpenJoystick)() |

## Return Value

Returns the player index, or -1 if it's not available.

## Remarks

For XInput controllers this returns the XInput user index. Many joysticks
will not be able to supply this information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

