###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorFromInstanceID

Return the [SDL_Sensor](SDL_Sensor.md) associated with an instance id.

## Syntax

```c
SDL_Sensor* SDL_SensorFromInstanceID(SDL_SensorID instance_id);

```

## Function Parameters

|                     |                             |
| ------------------- | --------------------------- |
| **instance_id**     | The sensor from instance id |

## Return Value

Returns an [SDL_Sensor](SDL_Sensor.md) object.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI.md)
