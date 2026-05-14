# SDL_HasSVE2

Determine whether the CPU has SVE2 (Scalable Vector Extension 2).

## Header File

Defined in [<SDL3/SDL_cpuinfo.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_cpuinfo.h)

## Syntax

```c
bool SDL_HasSVE2(void);
```

## Return Value

(bool) Returns true if the CPU has SVE2, false otherwise.

## Remarks

This is only relevant on ARM64 Linux. On other platforms it always returns
false.

## Version

This function is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCPUInfo](CategoryCPUInfo)

