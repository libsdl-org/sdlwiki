###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRealGamepadInstanceType

Get the type of a gamepad, ignoring any mapping override.

## Syntax

```c
SDL_GamepadType SDL_GetRealGamepadInstanceType(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                          |
| ------------------- | ------------------------ |
| **instance_id**     | the joystick instance ID |

## Return Value

Returns the gamepad type.

## Remarks

This can be called before any gamepads are opened.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

