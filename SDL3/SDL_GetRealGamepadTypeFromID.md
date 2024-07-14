###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRealGamepadTypeFromID

Get the type of a gamepad, ignoring any mapping override.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_GamepadType SDL_GetRealGamepadTypeFromID(SDL_JoystickID instance_id);
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

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetGamepadTypeFromID](SDL_GetGamepadTypeFromID)
- [SDL_GetGamepads](SDL_GetGamepads)
- [SDL_GetRealGamepadType](SDL_GetRealGamepadType)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

