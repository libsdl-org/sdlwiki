###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetType

Get the type of this currently opened controller

## Syntax

```c
SDL_GameControllerType SDL_GameControllerGetType(SDL_GameController *gamecontroller);

```

## Function Parameters

|                        |                                      |
| ---------------------- | ------------------------------------ |
| **gamecontroller**     | the game controller object to query. |

## Return Value

Returns the controller type.

## Remarks

This is the same name as returned by
[SDL_GameControllerTypeForIndex](SDL_GameControllerTypeForIndex.md)(), but it
takes a controller identifier instead of the (unstable) device index.

## Version

This function is available since SDL 2.0.12.

----
[CategoryAPI](CategoryAPI.md)
