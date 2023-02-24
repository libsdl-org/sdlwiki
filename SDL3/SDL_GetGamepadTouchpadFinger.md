###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadTouchpadFinger

Get the current state of a finger on a touchpad on a gamepad.

## Syntax

```c
int SDL_GetGamepadTouchpadFinger(SDL_Gamepad *gamepad, int touchpad, int finger, Uint8 *state, float *x, float *y, float *pressure);

```

## Function Parameters

|                  |                            |
| ---------------- | -------------------------- |
| **gamepad**      | a gamepad                  |
| **touchpad**     | a touchpad                 |
| **finger**       | a finger                   |
| **state**        | filled with state          |
| **x**            | filled with x position     |
| **y**            | filled with y position     |
| **pressure**     | filled with pressure value |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

