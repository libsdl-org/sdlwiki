###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetNumGamepadTouchpadFingers

Get the number of supported simultaneous fingers on a touchpad on a game gamepad.

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

----
[CategoryAPI](CategoryAPI)

