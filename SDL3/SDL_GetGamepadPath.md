###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadPath

Get the implementation-dependent path for an opened gamepad.

## Header File

Defined in [SDL_gamepad.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
const char* SDL_GetGamepadPath(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| **gamepad**     | a gamepad identifier previously returned by [SDL_OpenGamepad](SDL_OpenGamepad)() |

## Return Value

Returns the implementation dependent path for the gamepad, or NULL if there
is no path or the identifier passed is invalid.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetGamepadInstancePath](SDL_GetGamepadInstancePath)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

