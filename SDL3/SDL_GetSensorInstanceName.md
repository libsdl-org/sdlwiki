###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSensorInstanceName

Get the implementation dependent name of a sensor.

## Syntax

```c
const char* SDL_GetSensorInstanceName(SDL_SensorID instance_id);

```

## Function Parameters

|                     |                        |
| ------------------- | ---------------------- |
| **instance_id**     | the sensor instance ID |

## Return Value

Returns the sensor name, or NULL if `instance_id` is not valid

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

