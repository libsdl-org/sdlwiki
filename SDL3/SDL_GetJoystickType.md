###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickType

Get the type of an opened joystick.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_JoystickType SDL_GetJoystickType(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_OpenJoystick](SDL_OpenJoystick)() |

## Return Value

Returns the [SDL_JoystickType](SDL_JoystickType) of the selected joystick.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetJoystickInstanceType](SDL_GetJoystickInstanceType)

----
[CategoryAPI](CategoryAPI)

