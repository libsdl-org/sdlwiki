###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadInstancePlayerIndex

Get the player index of a gamepad.

## Syntax

```c
int SDL_GetGamepadInstancePlayerIndex(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                          |
| ------------------- | ------------------------ |
| **instance_id**     | the joystick instance ID |

## Return Value

Returns the player index of a gamepad, or -1 if it's not available

## Remarks

This can be called before any gamepads are opened.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadPlayerIndex](SDL_GetGamepadPlayerIndex)
* [SDL_OpenGamepad](SDL_OpenGamepad)

----
[CategoryAPI](CategoryAPI)

