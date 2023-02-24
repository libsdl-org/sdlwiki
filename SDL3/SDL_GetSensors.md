###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSensors

Get a list of currently connected sensors.

## Syntax

```c
SDL_SensorID* SDL_GetSensors(int *count);

```

## Function Parameters

|               |                                                         |
| ------------- | ------------------------------------------------------- |
| **count**     | a pointer filled in with the number of sensors returned |

## Return Value

Returns a 0 terminated array of sensor instance IDs which should be freed
with [SDL_free](SDL_free)(), or NULL on error; call
[SDL_GetError](SDL_GetError)() for more details.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

