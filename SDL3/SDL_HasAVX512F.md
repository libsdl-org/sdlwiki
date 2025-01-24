# SDL_HasAVX512F

Determine whether the CPU has AVX-512F (foundation) features.

## Header File

Defined in [<SDL3/SDL_cpuinfo.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_cpuinfo.h)

## Syntax

```c
bool SDL_HasAVX512F(void);
```

## Return Value

(bool) Returns true if the CPU has AVX-512F features or false if not.

## Remarks

This always returns false on CPUs that aren't using Intel instruction sets.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_HasAVX](SDL_HasAVX)
- [SDL_HasAVX2](SDL_HasAVX2)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCPUInfo](CategoryCPUInfo)

