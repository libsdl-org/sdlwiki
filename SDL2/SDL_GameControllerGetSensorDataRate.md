###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetSensorDataRate

Get the data rate (number of events per second) of a game controller sensor.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
float SDL_GameControllerGetSensorDataRate(SDL_GameController *gamecontroller, SDL_SensorType type);

```

## Function Parameters

|                        |                             |
| ---------------------- | --------------------------- |
| **gamecontroller**     | The controller to query     |
| **type**               | The type of sensor to query |

## Return Value

Return the data rate, or 0.0f if the data rate is not available.

## Version

This function is available since SDL 2.0.16.

----
[CategoryAPI](CategoryAPI)

