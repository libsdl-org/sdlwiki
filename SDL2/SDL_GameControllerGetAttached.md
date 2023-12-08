###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetAttached

Check if a controller has been opened and is currently connected.

## Syntax

```c
SDL_bool SDL_GameControllerGetAttached(SDL_GameController *gamecontroller);

```

## Function Parameters

|                        |                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------ |
| **gamecontroller**     | a game controller identifier previously returned by [SDL_GameControllerOpen](SDL_GameControllerOpen.md)() |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the controller has been opened and is
currently connected, or [SDL_FALSE](SDL_FALSE.md) if not.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GameControllerClose](SDL_GameControllerClose.md)
* [SDL_GameControllerOpen](SDL_GameControllerOpen.md)

----
[CategoryAPI](CategoryAPI.md)
