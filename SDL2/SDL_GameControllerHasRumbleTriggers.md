###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerHasRumbleTriggers

Query whether a game controller has rumble support on triggers.

## Syntax

```c
SDL_bool SDL_GameControllerHasRumbleTriggers(SDL_GameController *gamecontroller);

```

## Function Parameters

|                        |                         |
| ---------------------- | ----------------------- |
| **gamecontroller**     | The controller to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md), or [SDL_FALSE](SDL_FALSE.md) if this controller
does not have trigger rumble support

## Version

This function is available since SDL 2.0.18.

## Related Functions

* [SDL_GameControllerRumbleTriggers](SDL_GameControllerRumbleTriggers.md)

----
[CategoryAPI](CategoryAPI.md)
