###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetCPUCacheLineSize

Determine the L1 cache line size of the CPU.

## Header File

Defined in [<SDL3/SDL_cpuinfo.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_cpuinfo.h)

## Syntax

```c
int SDL_GetCPUCacheLineSize(void);
```

## Return Value

(int) Returns the L1 cache line size of the CPU, in bytes.

## Remarks

This is useful for determining multi-threaded structure padding or SIMD
prefetch sizes.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCPUInfo](CategoryCPUInfo)

