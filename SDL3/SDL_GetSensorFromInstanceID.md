###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSensorFromInstanceID

Return the [SDL_Sensor](SDL_Sensor) associated with an instance ID.

## Syntax

```c
SDL_Sensor* SDL_GetSensorFromInstanceID(SDL_SensorID instance_id);

```

## Function Parameters

|                     |                        |
| ------------------- | ---------------------- |
| **instance_id**     | the sensor instance ID |

## Return Value

Returns an [SDL_Sensor](SDL_Sensor) object.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

