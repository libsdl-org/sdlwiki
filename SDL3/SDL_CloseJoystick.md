###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CloseJoystick

Close a joystick previously opened with [SDL_OpenJoystick](SDL_OpenJoystick)().

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
void SDL_CloseJoystick(SDL_Joystick *joystick);
```

## Function Parameters

|                  |                              |
| ---------------- | ---------------------------- |
| **joystick**     | The joystick device to close |

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_OpenJoystick](SDL_OpenJoystick)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

