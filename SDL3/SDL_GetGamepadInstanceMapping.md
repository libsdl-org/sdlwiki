###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadInstanceMapping

Get the mapping of a gamepad.

## Syntax

```c
char* SDL_GetGamepadInstanceMapping(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                          |
| ------------------- | ------------------------ |
| **instance_id**     | the joystick instance ID |

## Return Value

Returns the mapping string. Must be freed with [SDL_free](SDL_free)().
Returns NULL if no mapping is available.

## Remarks

This can be called before any gamepads are opened.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

