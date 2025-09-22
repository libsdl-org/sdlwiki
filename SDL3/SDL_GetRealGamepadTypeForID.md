# SDL_GetRealGamepadTypeForID

Get the type of a gamepad, ignoring any mapping override.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_GamepadType SDL_GetRealGamepadTypeForID(SDL_JoystickID instance_id);
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

- [SDL_GetGamepadTypeForID](SDL_GetGamepadTypeForID)
- [SDL_GetGamepads](SDL_GetGamepads)
- [SDL_GetRealGamepadType](SDL_GetRealGamepadType)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

