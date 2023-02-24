###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickInstancePath

Get the implementation dependent path of a joystick.

## Syntax

```c
const char* SDL_GetJoystickInstancePath(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                          |
| ------------------- | ------------------------ |
| **instance_id**     | the joystick instance ID |

## Return Value

Returns the path of the selected joystick. If no path can be found, this
function returns NULL; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

This can be called before any joysticks are opened.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetJoystickPath](SDL_GetJoystickPath)
* [SDL_OpenJoystick](SDL_OpenJoystick)

----
[CategoryAPI](CategoryAPI)

