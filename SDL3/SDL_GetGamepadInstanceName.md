###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadInstanceName

Get the implementation dependent name of a gamepad.

## Syntax

```c
const char* SDL_GetGamepadInstanceName(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                          |
| ------------------- | ------------------------ |
| **instance_id**     | the joystick instance ID |

## Return Value

Returns the name of the selected gamepad. If no name can be found, this
function returns NULL; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

This can be called before any gamepads are opened.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadName](SDL_GetGamepadName)
* [SDL_OpenGamepad](SDL_OpenGamepad)

----
[CategoryAPI](CategoryAPI)

