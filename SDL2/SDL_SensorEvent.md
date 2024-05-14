###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorEvent

Sensor event structure (event.sensor.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_SensorEvent
{
    Uint32 type;        /**< SDL_SENSORUPDATE */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    Sint32 which;       /**< The instance ID of the sensor */
    float data[6];      /**< Up to 6 values from the sensor - additional values can be queried using SDL_SensorGetData() */
    Uint64 timestamp_us; /**< The timestamp of the sensor reading in microseconds, if the hardware provides this information. */
} SDL_SensorEvent;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents), [CategoryAPIStruct](CategoryAPIStruct), 

