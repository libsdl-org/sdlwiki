# SDL_HasRDTSC

Determine whether the CPU has the RDTSC instruction.

## Header File

Defined in [SDL_cpuinfo.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_cpuinfo.h)

## Syntax

```c
SDL_bool SDL_HasRDTSC(void);
```

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the CPU has the
RDTSC instruction or [SDL_FALSE](SDL_FALSE) if not.

## Remarks

This always returns false on CPUs that aren't using Intel instruction sets.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_Has3DNow](SDL_Has3DNow)
- [SDL_HasAltiVec](SDL_HasAltiVec)
- [SDL_HasAVX](SDL_HasAVX)
- [SDL_HasAVX2](SDL_HasAVX2)
- [SDL_HasMMX](SDL_HasMMX)
- [SDL_HasSSE](SDL_HasSSE)
- [SDL_HasSSE2](SDL_HasSSE2)
- [SDL_HasSSE3](SDL_HasSSE3)
- [SDL_HasSSE41](SDL_HasSSE41)
- [SDL_HasSSE42](SDL_HasSSE42)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCPUInfo](CategoryCPUInfo)

