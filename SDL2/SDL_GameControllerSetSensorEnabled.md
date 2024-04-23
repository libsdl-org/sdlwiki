###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerSetSensorEnabled

Set whether data reporting for a game controller sensor is enabled.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
int SDL_GameControllerSetSensorEnabled(SDL_GameController *gamecontroller, SDL_SensorType type, SDL_bool enabled);

```

## Function Parameters

|                        |                                          |
| ---------------------- | ---------------------------------------- |
| **gamecontroller**     | The controller to update                 |
| **type**               | The type of sensor to enable/disable     |
| **enabled**            | Whether data reporting should be enabled |

## Return Value

Returns 0 or -1 if an error occurred.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


