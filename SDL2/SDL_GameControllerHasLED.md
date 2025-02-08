# SDL_GameControllerHasLED

Query whether a game controller has an LED.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
SDL_bool SDL_GameControllerHasLED(SDL_GameController *gamecontroller);
```

## Function Parameters

|                                            |                    |                          |
| ------------------------------------------ | ------------------ | ------------------------ |
| [SDL_GameController](SDL_GameController) * | **gamecontroller** | The controller to query. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE), or
[SDL_FALSE](SDL_FALSE) if this controller does not have a modifiable LED.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

