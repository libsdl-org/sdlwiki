###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LockSensors

Locking for multi-threaded access to the sensor API

## Syntax

```c
void SDL_LockSensors(void);

```

## Remarks

If you are using the sensor API or handling events from multiple threads
you should use these locking functions to protect access to the sensors.

In particular, you are guaranteed that the sensor list won't change, so the
API functions that take a sensor index will be valid, and sensor events
will not be delivered.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI.md)
