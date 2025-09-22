# SDL_GetGamepadTypeForID

Get the type of a gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_GamepadType SDL_GetGamepadTypeForID(SDL_JoystickID instance_id);
```

## Function Parameters

|                                  |                 |                           |
| -------------------------------- | --------------- | ------------------------- |
| [SDL_JoystickID](SDL_JoystickID) | **instance_id** | the joystick instance ID. |

## Return Value

([SDL_GamepadType](SDL_GamepadType)) Returns the gamepad type.

## Remarks

This can be called before any gamepads are opened.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetGamepadType](SDL_GetGamepadType)
- [SDL_GetGamepads](SDL_GetGamepads)
- [SDL_GetRealGamepadTypeForID](SDL_GetRealGamepadTypeForID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

