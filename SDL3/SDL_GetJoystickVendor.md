###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickVendor

Get the USB vendor ID of an opened joystick, if available.

## Syntax

```c
Uint16 SDL_GetJoystickVendor(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_OpenJoystick](SDL_OpenJoystick)() |

## Return Value

Returns the USB vendor ID of the selected joystick, or 0 if unavailable.

## Remarks

If the vendor ID isn't available this function returns 0.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

