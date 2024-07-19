###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadBindings

Get the SDL joystick layer bindings for a gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
const SDL_GamepadBinding * const * SDL_GetGamepadBindings(SDL_Gamepad *gamepad, int *count);
```

## Function Parameters

|                              |             |                                                           |
| ---------------------------- | ----------- | --------------------------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad** | a gamepad.                                                |
| int *                        | **count**   | a pointer filled in with the number of bindings returned. |

## Return Value

(const [SDL_GamepadBinding](SDL_GamepadBinding) * const *) Returns a NULL
terminated array of pointers to bindings or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This returns temporary memory which will be automatically freed later, and
can be claimed with [SDL_ClaimTemporaryMemory](SDL_ClaimTemporaryMemory)().

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

