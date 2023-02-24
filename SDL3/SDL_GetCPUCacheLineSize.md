###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCPUCacheLineSize

Determine the L1 cache line size of the CPU.

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

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryCPU](CategoryCPU)


