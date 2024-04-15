###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadBindings

Get the SDL joystick layer bindings for a gamepad.

## Header File

Defined in [SDL_gamepad.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
extern DECLSPEC SDL_GamepadBinding **SDLCALL SDL_GetGamepadBindings(SDL_Gamepad *gamepad, int *count);

```

## Function Parameters

|                 |                                                          |
| --------------- | -------------------------------------------------------- |
| **gamepad**     | a gamepad                                                |
| **count**       | a pointer filled in with the number of bindings returned |

## Return Value

Returns a NULL terminated array of pointers to bindings which should be
freed with [SDL_free](SDL_free)(), or NULL on error; call
[SDL_GetError](SDL_GetError)() for more details.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

