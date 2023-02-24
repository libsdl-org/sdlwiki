###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UpdateSensors

Update the current state of the open sensors.

## Syntax

```c
void SDL_UpdateSensors(void);

```

## Remarks

This is called automatically by the event loop if sensor events are
enabled.

This needs to be called from the thread that initialized the sensor
subsystem.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

