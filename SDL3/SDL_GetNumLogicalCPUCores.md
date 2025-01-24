# SDL_GetNumLogicalCPUCores

Get the number of logical CPU cores available.

## Header File

Defined in [<SDL3/SDL_cpuinfo.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_cpuinfo.h)

## Syntax

```c
int SDL_GetNumLogicalCPUCores(void);
```

## Return Value

(int) Returns the total number of logical CPU cores. On CPUs that include
technologies such as hyperthreading, the number of logical cores may be
more than the number of physical cores.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCPUInfo](CategoryCPUInfo)

