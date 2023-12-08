###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickType

Get the type of an opened joystick.

## Syntax

```c
SDL_JoystickType SDL_GetJoystickType(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick.md) obtained from [SDL_OpenJoystick](SDL_OpenJoystick.md)() |

## Return Value

Returns the [SDL_JoystickType](SDL_JoystickType.md) of the selected joystick.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
