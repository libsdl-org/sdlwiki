###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HasLASX

Determine whether the CPU has LASX (LOONGARCH SIMD) features.

## Header File

Defined in [<SDL3/SDL_cpuinfo.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_cpuinfo.h)

## Syntax

```c
bool SDL_HasLASX(void);
```

## Return Value

(bool) Returns true if the CPU has LOONGARCH LASX features or false if not.

## Remarks

This always returns false on CPUs that aren't using LOONGARCH instruction
sets.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCPUInfo](CategoryCPUInfo)

