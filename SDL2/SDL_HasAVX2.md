###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasAVX2

Determine whether the CPU has AVX2 features.

## Syntax

```c
SDL_bool SDL_HasAVX2(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the CPU has AVX2 features or
[SDL_FALSE](SDL_FALSE.md) if not.

## Remarks

This always returns false on CPUs that aren't using Intel instruction sets.

## Version

This function is available since SDL 2.0.4.

## Related Functions

* [SDL_Has3DNow](SDL_Has3DNow.md)
* [SDL_HasAltiVec](SDL_HasAltiVec.md)
* [SDL_HasAVX](SDL_HasAVX.md)
* [SDL_HasMMX](SDL_HasMMX.md)
* [SDL_HasRDTSC](SDL_HasRDTSC.md)
* [SDL_HasSSE](SDL_HasSSE.md)
* [SDL_HasSSE2](SDL_HasSSE2.md)
* [SDL_HasSSE3](SDL_HasSSE3.md)
* [SDL_HasSSE41](SDL_HasSSE41.md)
* [SDL_HasSSE42](SDL_HasSSE42.md)

----
[CategoryAPI](CategoryAPI.md)
