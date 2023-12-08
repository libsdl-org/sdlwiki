###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerHasLED

Query whether a game controller has an LED.

## Syntax

```c
SDL_bool SDL_GameControllerHasLED(SDL_GameController *gamecontroller);

```

## Function Parameters

|                        |                         |
| ---------------------- | ----------------------- |
| **gamecontroller**     | The controller to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md), or [SDL_FALSE](SDL_FALSE.md) if this controller
does not have a modifiable LED

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI.md)
