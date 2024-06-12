###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerSetPlayerIndex

Set the player index of an opened game controller.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
void SDL_GameControllerSetPlayerIndex(SDL_GameController *gamecontroller, int player_index);
```

## Function Parameters

|                                            |                    |                                                                                                      |
| ------------------------------------------ | ------------------ | ---------------------------------------------------------------------------------------------------- |
| [SDL_GameController](SDL_GameController) * | **gamecontroller** | the game controller object to adjust.                                                                |
| int                                        | **player_index**   | Player index to assign to this controller, or -1 to clear the player index and turn off player LEDs. |

## Version

This function is available since SDL 2.0.12.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

