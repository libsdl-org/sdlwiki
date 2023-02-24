###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasARMSIMD

Determine whether the CPU has ARM SIMD (ARMv6) features.

## Syntax

```c
SDL_bool SDL_HasARMSIMD(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the CPU has ARM SIMD features or
[SDL_FALSE](SDL_FALSE) if not.

## Remarks

This is different from ARM NEON, which is a different instruction set.

This always returns false on CPUs that aren't using ARM instruction sets.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HasNEON](SDL_HasNEON)

----
[CategoryAPI](CategoryAPI)

