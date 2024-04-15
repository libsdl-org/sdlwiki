###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SensorEvent

Sensor event structure (event.sensor.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
typedef struct SDL_SensorEvent
{
    SDL_EventType type; /**< ::SDL_EVENT_SENSOR_UPDATE */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_SensorID which; /**< The instance ID of the sensor */
    float data[6];      /**< Up to 6 values from the sensor - additional values can be queried using SDL_GetSensorData() */
    Uint64 sensor_timestamp; /**< The timestamp of the sensor reading in nanoseconds, not necessarily synchronized with the system clock */
} SDL_SensorEvent;
```

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

