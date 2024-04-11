###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickPath

Get the implementation dependent path of a joystick.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
const char* SDL_JoystickPath(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_JoystickOpen](SDL_JoystickOpen)() |

## Return Value

Returns the path of the selected joystick. If no path can be found, this
function returns NULL; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 2.24.0.

## See Also

* [SDL_JoystickPathForIndex](SDL_JoystickPathForIndex)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

