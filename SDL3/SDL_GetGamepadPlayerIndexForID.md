# SDL_GetGamepadPlayerIndexForID

Get the player index of a gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
int SDL_GetGamepadPlayerIndexForID(SDL_JoystickID instance_id);
```

## Function Parameters

|                                  |                 |                           |
| -------------------------------- | --------------- | ------------------------- |
| [SDL_JoystickID](SDL_JoystickID) | **instance_id** | the joystick instance ID. |

## Return Value

(int) Returns the player index of a gamepad, or -1 if it's not available.

## Remarks

This can be called before any gamepads are opened.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetGamepadPlayerIndex](SDL_GetGamepadPlayerIndex)
- [SDL_GetGamepads](SDL_GetGamepads)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

