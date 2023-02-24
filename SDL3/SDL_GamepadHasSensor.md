###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GamepadHasSensor

Return whether a gamepad has a particular sensor.

## Syntax

```c
SDL_bool SDL_GamepadHasSensor(SDL_Gamepad *gamepad, SDL_SensorType type);

```

## Function Parameters

|                 |                             |
| --------------- | --------------------------- |
| **gamepad**     | The gamepad to query        |
| **type**        | The type of sensor to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the sensor exists, [SDL_FALSE](SDL_FALSE)
otherwise.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

