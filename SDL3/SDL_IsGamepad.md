###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_IsGamepad

Check if the given joystick is supported by the gamepad interface.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
bool SDL_IsGamepad(SDL_JoystickID instance_id);
```

## Function Parameters

|                                  |                 |                           |
| -------------------------------- | --------------- | ------------------------- |
| [SDL_JoystickID](SDL_JoystickID) | **instance_id** | the joystick instance ID. |

## Return Value

(bool) Returns true if the given joystick is supported by the gamepad
interface, false if it isn't or it's an invalid index.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetJoysticks](SDL_GetJoysticks)
- [SDL_OpenGamepad](SDL_OpenGamepad)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

