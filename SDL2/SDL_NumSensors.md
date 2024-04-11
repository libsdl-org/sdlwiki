###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_NumSensors

Count the number of sensors attached to the system right now.

## Header File

Defined in [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_sensor.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_NumSensors(void);

```

## Return Value

Returns the number of sensors detected.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

