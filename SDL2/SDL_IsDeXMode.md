###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_IsDeXMode

Query if the application is running on a Samsung DeX docking station.

## Syntax

```c
SDL_bool SDL_IsDeXMode(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if this is a DeX docking station,
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI.md)
