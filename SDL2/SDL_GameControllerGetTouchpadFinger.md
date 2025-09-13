# SDL_GameControllerGetTouchpadFinger

Get the current state of a finger on a touchpad on a game controller.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
int SDL_GameControllerGetTouchpadFinger(SDL_GameController *gamecontroller, int touchpad, int finger, Uint8 *state, float *x, float *y, float *pressure);
```

## Function Parameters

|                                            |                    |                                         |
| ------------------------------------------ | ------------------ | --------------------------------------- |
| [SDL_GameController](SDL_GameController) * | **gamecontroller** | a controller.                           |
| int                                        | **touchpad**       | a touchpad.                             |
| int                                        | **finger**         | a finger.                               |
| Uint8 *                                    | **state**          | a pointer filled with the finger state. |
| float *                                    | **x**              | a pointer filled with the x position.   |
| float *                                    | **y**              | a pointer filled with the y position.   |
| float *                                    | **pressure**       | a pointer filled with pressure value.   |

## Return Value

(int) Returns 0 on success or negative on failure.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

