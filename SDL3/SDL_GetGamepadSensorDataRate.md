###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadSensorDataRate

Get the data rate (number of events per second) of a gamepad sensor.

## Header File

Defined in [SDL_gamepad.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
float SDL_GetGamepadSensorDataRate(SDL_Gamepad *gamepad, SDL_SensorType type);

```

## Function Parameters

|                 |                             |
| --------------- | --------------------------- |
| **gamepad**     | The gamepad to query        |
| **type**        | The type of sensor to query |

## Return Value

Returns the data rate, or 0.0f if the data rate is not available.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

