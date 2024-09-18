###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadTouchpadFinger

Get the current state of a finger on a touchpad on a gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
bool SDL_GetGamepadTouchpadFinger(SDL_Gamepad *gamepad, int touchpad, int finger, bool *down, float *x, float *y, float *pressure);
```

## Function Parameters

|                              |              |                                                                                                          |
| ---------------------------- | ------------ | -------------------------------------------------------------------------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad**  | a gamepad.                                                                                               |
| int                          | **touchpad** | a touchpad.                                                                                              |
| int                          | **finger**   | a finger.                                                                                                |
| bool *                       | **down**     | a pointer filled with true if the finger is down, false otherwise, may be NULL.                          |
| float *                      | **x**        | a pointer filled with the x position, normalized 0 to 1, with the origin in the upper left, may be NULL. |
| float *                      | **y**        | a pointer filled with the y position, normalized 0 to 1, with the origin in the upper left, may be NULL. |
| float *                      | **pressure** | a pointer filled with pressure value, may be NULL.                                                       |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetNumGamepadTouchpadFingers](SDL_GetNumGamepadTouchpadFingers)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

