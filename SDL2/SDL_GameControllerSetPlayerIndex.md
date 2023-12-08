###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerSetPlayerIndex

Set the player index of an opened game controller.

## Syntax

```c
void SDL_GameControllerSetPlayerIndex(SDL_GameController *gamecontroller, int player_index);

```

## Function Parameters

|                        |                                                                                                      |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| **gamecontroller**     | the game controller object to adjust.                                                                |
| **player_index**       | Player index to assign to this controller, or -1 to clear the player index and turn off player LEDs. |

## Version

This function is available since SDL 2.0.12.

----
[CategoryAPI](CategoryAPI.md)
