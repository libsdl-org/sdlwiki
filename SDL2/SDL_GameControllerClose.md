# SDL_GameControllerClose

Close a game controller previously opened with [SDL_GameControllerOpen](SDL_GameControllerOpen)().

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
void SDL_GameControllerClose(SDL_GameController *gamecontroller);
```

## Function Parameters

|                                            |                    |                                                                                                         |
| ------------------------------------------ | ------------------ | ------------------------------------------------------------------------------------------------------- |
| [SDL_GameController](SDL_GameController) * | **gamecontroller** | a game controller identifier previously returned by [SDL_GameControllerOpen](SDL_GameControllerOpen)(). |

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GameControllerOpen](SDL_GameControllerOpen)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

