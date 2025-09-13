# SDL_GameControllerGetNumTouchpadFingers

Get the number of supported simultaneous fingers on a touchpad on a game controller.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
int SDL_GameControllerGetNumTouchpadFingers(SDL_GameController *gamecontroller, int touchpad);
```

## Function Parameters

|                                            |                    |               |
| ------------------------------------------ | ------------------ | ------------- |
| [SDL_GameController](SDL_GameController) * | **gamecontroller** | a controller. |
| int                                        | **touchpad**       | a touchpad.   |

## Return Value

(int) Returns number of supported simultaneous fingers.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

