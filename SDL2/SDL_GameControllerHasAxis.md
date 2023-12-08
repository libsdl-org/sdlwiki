###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerHasAxis

Query whether a game controller has a given axis.

## Syntax

```c
extern DECLSPEC SDL_bool SDLCALL
SDL_GameControllerHasAxis(SDL_GameController *gamecontroller, SDL_GameControllerAxis axis);

```

## Function Parameters

|                        |                                                                                |
| ---------------------- | ------------------------------------------------------------------------------ |
| **gamecontroller**     | a game controller                                                              |
| **axis**               | an axis enum value (an [SDL_GameControllerAxis](SDL_GameControllerAxis.md) value) |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the controller has this axis,
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Remarks

This merely reports whether the controller's mapping defined this axis, as
that is all the information SDL has about the physical device.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI.md)
