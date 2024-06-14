###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerHasAxis

Query whether a game controller has a given axis.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
extern DECLSPEC SDL_bool SDLCALL
SDL_GameControllerHasAxis(SDL_GameController *gamecontroller, SDL_GameControllerAxis axis);
```

## Function Parameters

|                                                  |                    |                                                                                 |
| ------------------------------------------------ | ------------------ | ------------------------------------------------------------------------------- |
| [SDL_GameController](SDL_GameController) *       | **gamecontroller** | a game controller.                                                              |
| [SDL_GameControllerAxis](SDL_GameControllerAxis) | **axis**           | an axis enum value (an [SDL_GameControllerAxis](SDL_GameControllerAxis) value). |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the controller has
this axis, [SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

This merely reports whether the controller's mapping defined this axis, as
that is all the information SDL has about the physical device.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

