###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
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

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetGamepadType](SDL_GetGamepadType)
- [SDL_GetGamepads](SDL_GetGamepads)
- [SDL_GetRealGamepadTypeForID](SDL_GetRealGamepadTypeForID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

