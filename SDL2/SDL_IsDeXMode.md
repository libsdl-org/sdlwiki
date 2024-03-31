###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_IsDeXMode

Query if the application is running on a Samsung DeX docking station.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_bool SDL_IsDeXMode(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if this is a DeX docking station,
[SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI)

