###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_IsGamepad

Check if the given joystick is supported by the gamepad interface.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_bool SDL_IsGamepad(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                          |
| ------------------- | ------------------------ |
| **instance_id**     | the joystick instance ID |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the given joystick is supported by the
gamepad interface, [SDL_FALSE](SDL_FALSE) if it isn't or it's an invalid
index.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetJoysticks](SDL_GetJoysticks)
- [SDL_OpenGamepad](SDL_OpenGamepad)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

