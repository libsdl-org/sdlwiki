###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadInstanceVendor

Get the USB vendor ID of a gamepad, if available.

## Syntax

```c
Uint16 SDL_GetGamepadInstanceVendor(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                          |
| ------------------- | ------------------------ |
| **instance_id**     | the joystick instance ID |

## Return Value

Returns the USB vendor ID of the selected gamepad. If called on an invalid
index, this function returns zero

## Remarks

This can be called before any gamepads are opened. If the vendor ID isn't
available this function returns 0.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

