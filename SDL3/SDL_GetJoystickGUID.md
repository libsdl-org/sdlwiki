###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickGUID

Get the implementation-dependent GUID for the joystick.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_JoystickGUID SDL_GetJoystickGUID(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_OpenJoystick](SDL_OpenJoystick)() |

## Return Value

Returns the GUID of the given joystick. If called on an invalid index, this
function returns a zero GUID; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

This function requires an open joystick.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetJoystickInstanceGUID](SDL_GetJoystickInstanceGUID)
* [SDL_GetJoystickGUIDString](SDL_GetJoystickGUIDString)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

