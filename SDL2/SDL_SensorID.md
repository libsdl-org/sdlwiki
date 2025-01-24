# SDL_SensorID

This is a unique ID for a sensor for the time it is connected to the system, and is never reused for the lifetime of the application.

## Header File

Defined in [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_sensor.h)

## Syntax

```c
typedef Sint32 SDL_SensorID;
```

## Remarks

The ID value starts at 0 and increments from there. The value -1 is an
invalid ID.





----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySensor](CategorySensor)

