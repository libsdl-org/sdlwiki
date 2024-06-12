###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerSetLED

Update a game controller's LED color.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
int SDL_GameControllerSetLED(SDL_GameController *gamecontroller, Uint8 red, Uint8 green, Uint8 blue);
```

## Function Parameters

|                                            |                    |                                |
| ------------------------------------------ | ------------------ | ------------------------------ |
| [SDL_GameController](SDL_GameController) * | **gamecontroller** | The controller to update       |
| Uint8                                      | **red**            | The intensity of the red LED   |
| Uint8                                      | **green**          | The intensity of the green LED |
| Uint8                                      | **blue**           | The intensity of the blue LED  |

## Return Value

(int) Returns 0, or -1 if this controller does not have a modifiable LED

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

