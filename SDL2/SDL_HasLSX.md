###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasLSX

Determine whether the CPU has LSX (LOONGARCH SIMD) features.

## Syntax

```c
SDL_bool SDL_HasLSX(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the CPU has LOONGARCH LSX features or
[SDL_FALSE](SDL_FALSE) if not.

## Remarks

This always returns false on CPUs that aren't using LOONGARCH instruction
sets.

## Version

This function is available since SDL 2.24.0.

----
[CategoryAPI](CategoryAPI)

