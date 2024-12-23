###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetGamepadSensorDataRate

Get the data rate (number of events per second) of a gamepad sensor.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
float SDL_GetGamepadSensorDataRate(SDL_Gamepad *gamepad, SDL_SensorType type);
```

## Function Parameters

|                                  |             |                              |
| -------------------------------- | ----------- | ---------------------------- |
| [SDL_Gamepad](SDL_Gamepad) *     | **gamepad** | the gamepad to query.        |
| [SDL_SensorType](SDL_SensorType) | **type**    | the type of sensor to query. |

## Return Value

(float) Returns the data rate, or 0.0f if the data rate is not available.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

