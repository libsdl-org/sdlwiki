###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadInstanceProductVersion

Get the product version of a gamepad, if available.

## Syntax

```c
Uint16 SDL_GetGamepadInstanceProductVersion(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                          |
| ------------------- | ------------------------ |
| **instance_id**     | the joystick instance ID |

## Return Value

Returns the product version of the selected gamepad. If called on an
invalid index, this function returns zero

## Remarks

This can be called before any gamepads are opened. If the product version
isn't available this function returns 0.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

