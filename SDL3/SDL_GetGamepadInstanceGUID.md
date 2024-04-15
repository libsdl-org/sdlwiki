###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadInstanceGUID

Get the implementation-dependent GUID of a gamepad.

## Header File

Defined in [SDL_gamepad.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
SDL_JoystickGUID SDL_GetGamepadInstanceGUID(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                          |
| ------------------- | ------------------------ |
| **instance_id**     | the joystick instance ID |

## Return Value

Returns the GUID of the selected gamepad. If called on an invalid index,
this function returns a zero GUID

## Remarks

This can be called before any gamepads are opened.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetGamepadGUID](SDL_GetGamepadGUID)
* [SDL_GetGamepadGUIDString](SDL_GetGamepadGUIDString)
* [SDL_GetGamepads](SDL_GetGamepads)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

