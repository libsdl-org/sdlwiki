###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetNumGamepadTouchpadFingers

Get the number of supported simultaneous fingers on a touchpad on a game gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
int SDL_GetNumGamepadTouchpadFingers(SDL_Gamepad *gamepad, int touchpad);

```

## Function Parameters

|                  |            |
| ---------------- | ---------- |
| **gamepad**      | a gamepad  |
| **touchpad**     | a touchpad |

## Return Value

Returns number of supported simultaneous fingers

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetGamepadTouchpadFinger](SDL_GetGamepadTouchpadFinger)
- [SDL_GetNumGamepadTouchpads](SDL_GetNumGamepadTouchpads)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

