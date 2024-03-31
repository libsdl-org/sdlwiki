###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_JoystickConnected

Get the status of a specified joystick.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_bool SDL_JoystickConnected(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **joystick**     | the joystick to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the joystick has been opened,
[SDL_FALSE](SDL_FALSE) if it has not; call [SDL_GetError](SDL_GetError)()
for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

