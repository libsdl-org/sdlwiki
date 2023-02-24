###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickProductVersion

Get the product version of an opened joystick, if available.

## Syntax

```c
Uint16 SDL_GetJoystickProductVersion(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_OpenJoystick](SDL_OpenJoystick)() |

## Return Value

Returns the product version of the selected joystick, or 0 if unavailable.

## Remarks

If the product version isn't available this function returns 0.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

