# SDL_GetGamepadProductForID

Get the USB product ID of a gamepad, if available.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
Uint16 SDL_GetGamepadProductForID(SDL_JoystickID instance_id);
```

## Function Parameters

|                                  |                 |                           |
| -------------------------------- | --------------- | ------------------------- |
| [SDL_JoystickID](SDL_JoystickID) | **instance_id** | the joystick instance ID. |

## Return Value

([Uint16](Uint16)) Returns the USB product ID of the selected gamepad. If
called on an invalid index, this function returns zero.

## Remarks

This can be called before any gamepads are opened. If the product ID isn't
available this function returns 0.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetGamepadProduct](SDL_GetGamepadProduct)
- [SDL_GetGamepads](SDL_GetGamepads)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

