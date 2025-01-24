# SDL_JoystickConnected

Get the status of a specified joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
bool SDL_JoystickConnected(SDL_Joystick *joystick);
```

## Function Parameters

|                                |              |                        |
| ------------------------------ | ------------ | ---------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the joystick to query. |

## Return Value

(bool) Returns true if the joystick has been opened, false if it has not;
call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

