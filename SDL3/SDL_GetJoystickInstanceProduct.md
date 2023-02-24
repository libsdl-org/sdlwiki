###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickInstanceProduct

Get the USB product ID of a joystick, if available.

## Syntax

```c
Uint16 SDL_GetJoystickInstanceProduct(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                          |
| ------------------- | ------------------------ |
| **instance_id**     | the joystick instance ID |

## Return Value

Returns the USB product ID of the selected joystick. If called on an
invalid index, this function returns zero

## Remarks

This can be called before any joysticks are opened. If the product ID isn't
available this function returns 0.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

