###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetCPUCacheLineSize

Determine the L1 cache line size of the CPU.

## Header File

Defined in [SDL_cpuinfo.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_cpuinfo.h)

## Syntax

```c
int SDL_GetCPUCacheLineSize(void);

```

## Return Value

Returns the L1 cache line size of the CPU, in bytes.

## Remarks

This is useful for determining multi-threaded structure padding or SIMD
prefetch sizes.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

