###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerClose

Close a game controller previously opened with [SDL_GameControllerOpen](SDL_GameControllerOpen)().

## Syntax

```c
void SDL_GameControllerClose(SDL_GameController *gamecontroller);

```

## Function Parameters

|                        |                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------ |
| **gamecontroller**     | a game controller identifier previously returned by [SDL_GameControllerOpen](SDL_GameControllerOpen)() |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GameControllerOpen](SDL_GameControllerOpen)

----
[CategoryAPI](CategoryAPI)

