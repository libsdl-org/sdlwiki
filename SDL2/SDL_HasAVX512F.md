###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasAVX512F

Determine whether the CPU has AVX-512F (foundation) features.

## Syntax

```c
SDL_bool SDL_HasAVX512F(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the CPU has AVX-512F features or
[SDL_FALSE](SDL_FALSE.md) if not.

## Remarks

This always returns false on CPUs that aren't using Intel instruction sets.

## Version

This function is available since SDL 2.0.9.

## Related Functions

* [SDL_HasAVX](SDL_HasAVX.md)

----
[CategoryAPI](CategoryAPI.md)
