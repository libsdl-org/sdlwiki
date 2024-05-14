###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetSensorData

Get the current state of a game controller sensor.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
int SDL_GameControllerGetSensorData(SDL_GameController *gamecontroller, SDL_SensorType type, float *data, int num_values);

```

## Function Parameters

|                        |                                                |
| ---------------------- | ---------------------------------------------- |
| **gamecontroller**     | The controller to query                        |
| **type**               | The type of sensor to query                    |
| **data**               | A pointer filled with the current sensor state |
| **num_values**         | The number of values to write to data          |

## Return Value

Return 0 or -1 if an error occurred.

## Remarks

The number of values and interpretation of the data is sensor dependent.
See [SDL_sensor](SDL_sensor).h for the details for each type of sensor.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

