###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerHasRumble

Query whether a game controller has rumble support.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
SDL_bool SDL_GameControllerHasRumble(SDL_GameController *gamecontroller);
```

## Function Parameters

|                                            |                    |                          |
| ------------------------------------------ | ------------------ | ------------------------ |
| [SDL_GameController](SDL_GameController) * | **gamecontroller** | The controller to query. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE), or
[SDL_FALSE](SDL_FALSE) if this controller does not have rumble support.

## Version

This function is available since SDL 2.0.18.

## See Also

- [SDL_GameControllerRumble](SDL_GameControllerRumble)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

