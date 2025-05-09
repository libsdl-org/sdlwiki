# SDL_HasAltiVec

Determine whether the CPU has AltiVec features.

## Header File

Defined in [<SDL3/SDL_cpuinfo.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_cpuinfo.h)

## Syntax

```c
bool SDL_HasAltiVec(void);
```

## Return Value

(bool) Returns true if the CPU has AltiVec features or false if not.

## Remarks

This always returns false on CPUs that aren't using PowerPC instruction
sets.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCPUInfo](CategoryCPUInfo)

