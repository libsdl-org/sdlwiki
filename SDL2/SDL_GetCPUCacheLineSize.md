# SDL_GetCPUCacheLineSize

Determine the L1 cache line size of the CPU.

## Header File

Defined in [SDL_cpuinfo.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_cpuinfo.h)

## Syntax

```c
int SDL_GetCPUCacheLineSize(void);
```

## Return Value

(int) Returns the L1 cache line size of the CPU, in bytes.

## Remarks

This is useful for determining multi-threaded structure padding or SIMD
prefetch sizes.

## Version

This function is available since SDL 2.0.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCPUInfo](CategoryCPUInfo)

