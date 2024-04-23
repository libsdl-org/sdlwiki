###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ControllerSensorEvent

Game controller sensor event structure (event.csensor.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_ControllerSensorEvent
{
    Uint32 type;        /**< SDL_CONTROLLERSENSORUPDATE */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    SDL_JoystickID which; /**< The joystick instance id */
    Sint32 sensor;      /**< The type of the sensor, one of the values of SDL_SensorType */
    float data[3];      /**< Up to 3 values from the sensor, as defined in SDL_sensor.h */
    Uint64 timestamp_us; /**< The timestamp of the sensor reading in microseconds, if the hardware provides this information. */
} SDL_ControllerSensorEvent;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

