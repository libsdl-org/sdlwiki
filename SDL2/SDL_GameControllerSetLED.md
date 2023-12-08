###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerSetLED

Update a game controller's LED color.

## Syntax

```c
int SDL_GameControllerSetLED(SDL_GameController *gamecontroller, Uint8 red, Uint8 green, Uint8 blue);

```

## Function Parameters

|                        |                                |
| ---------------------- | ------------------------------ |
| **gamecontroller**     | The controller to update       |
| **red**                | The intensity of the red LED   |
| **green**              | The intensity of the green LED |
| **blue**               | The intensity of the blue LED  |

## Return Value

Returns 0, or -1 if this controller does not have a modifiable LED

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI.md)
