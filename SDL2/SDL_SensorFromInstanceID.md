###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorFromInstanceID

Return the [SDL_Sensor](SDL_Sensor) associated with an instance id.

## Header File

Defined in [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_sensor.h)

## Syntax

```c
SDL_Sensor* SDL_SensorFromInstanceID(SDL_SensorID instance_id);
```

## Function Parameters

|                              |                 |                              |
| ---------------------------- | --------------- | ---------------------------- |
| [SDL_SensorID](SDL_SensorID) | **instance_id** | The sensor from instance id. |

## Return Value

([SDL_Sensor](SDL_Sensor) *) Returns an [SDL_Sensor](SDL_Sensor) object.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySensor](CategorySensor)

