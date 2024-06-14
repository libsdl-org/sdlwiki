###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetSensorDataWithTimestamp

Get the current state of a game controller sensor with the timestamp of the last update.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
int SDL_GameControllerGetSensorDataWithTimestamp(SDL_GameController *gamecontroller, SDL_SensorType type, Uint64 *timestamp, float *data, int num_values);
```

## Function Parameters

|                                            |                    |                                                                                                              |
| ------------------------------------------ | ------------------ | ------------------------------------------------------------------------------------------------------------ |
| [SDL_GameController](SDL_GameController) * | **gamecontroller** | The controller to query.                                                                                     |
| [SDL_SensorType](SDL_SensorType)           | **type**           | The type of sensor to query.                                                                                 |
| Uint64 *                                   | **timestamp**      | A pointer filled with the timestamp in microseconds of the current sensor reading if available, or 0 if not. |
| float *                                    | **data**           | A pointer filled with the current sensor state.                                                              |
| int                                        | **num_values**     | The number of values to write to data.                                                                       |

## Return Value

(int) Return 0 or -1 if an error occurred.

## Remarks

The number of values and interpretation of the data is sensor dependent.
See [SDL_sensor](SDL_sensor).h for the details for each type of sensor.

## Version

This function is available since SDL 2.26.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

