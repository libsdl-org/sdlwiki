###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasARMSIMD

Determine whether the CPU has ARM SIMD (ARMv6) features.

## Syntax

```c
SDL_bool SDL_HasARMSIMD(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the CPU has ARM SIMD features or
[SDL_FALSE](SDL_FALSE.md) if not.

## Remarks

This is different from ARM NEON, which is a different instruction set.

This always returns false on CPUs that aren't using ARM instruction sets.

## Version

This function is available since SDL 2.0.12.

## Related Functions

* [SDL_HasNEON](SDL_HasNEON.md)

----
[CategoryAPI](CategoryAPI.md)
