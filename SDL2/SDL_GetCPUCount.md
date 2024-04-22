###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetCPUCount

Get the number of CPU cores available.

## Header File

Defined in [SDL_cpuinfo.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_cpuinfo.h)

## Syntax

```c
int SDL_GetCPUCount(void);

```

## Return Value

Returns the total number of logical CPU cores. On CPUs that include
technologies such as hyperthreading, the number of logical cores may be
more than the number of physical cores.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

