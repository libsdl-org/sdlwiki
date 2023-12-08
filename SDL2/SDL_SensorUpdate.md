###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SensorUpdate

Update the current state of the open sensors.

## Syntax

```c
void SDL_SensorUpdate(void);

```

## Remarks

This is called automatically by the event loop if sensor events are
enabled.

This needs to be called from the thread that initialized the sensor
subsystem.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI.md)
