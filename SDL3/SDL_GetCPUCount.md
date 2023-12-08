###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCPUCount

Get the number of CPU cores available.

## Syntax

```c
int SDL_GetCPUCount(void);

```

## Return Value

Returns the total number of logical CPU cores. On CPUs that include
technologies such as hyperthreading, the number of logical cores may be
more than the number of physical cores.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
SDL_Log("Number of logical CPU cores: %d", SDL_GetCPUCount());
```

----
[CategoryAPI](CategoryAPI.md), [CategoryCPU](CategoryCPU.md)
