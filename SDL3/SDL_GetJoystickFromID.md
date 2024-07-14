###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickFromID

Get the [SDL_Joystick](SDL_Joystick) associated with an instance ID, if it has been opened.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_Joystick* SDL_GetJoystickFromID(SDL_JoystickID instance_id);
```

## Function Parameters

|                                  |                 |                                                              |
| -------------------------------- | --------------- | ------------------------------------------------------------ |
| [SDL_JoystickID](SDL_JoystickID) | **instance_id** | the instance ID to get the [SDL_Joystick](SDL_Joystick) for. |

## Return Value

([SDL_Joystick](SDL_Joystick) *) Returns an [SDL_Joystick](SDL_Joystick) on
success or NULL on failure or if it hasn't been opened yet; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

