# SDL_GetCPUCount

Get the number of CPU cores available.

## Header File

Defined in [SDL_cpuinfo.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_cpuinfo.h)

## Syntax

```c
int SDL_GetCPUCount(void);
```

## Return Value

(int) Returns the total number of logical CPU cores. On CPUs that include
technologies such as hyperthreading, the number of logical cores may be
more than the number of physical cores.

## Version

This function is available since SDL 2.0.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCPUInfo](CategoryCPUInfo)

