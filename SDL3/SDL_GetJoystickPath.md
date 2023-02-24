###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickPath

Get the implementation dependent path of a joystick.

## Syntax

```c
const char* SDL_GetJoystickPath(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_OpenJoystick](SDL_OpenJoystick)() |

## Return Value

Returns the path of the selected joystick. If no path can be found, this
function returns NULL; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetJoystickInstancePath](SDL_GetJoystickInstancePath)

----
[CategoryAPI](CategoryAPI)

