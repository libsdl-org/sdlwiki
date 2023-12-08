###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HasAltiVec](SDL_HasAltiVec.md)
* [SDL_HasAVX](SDL_HasAVX.md)
* [SDL_HasAVX2](SDL_HasAVX2.md)
* [SDL_HasMMX](SDL_HasMMX.md)
* [SDL_HasSSE](SDL_HasSSE.md)
* [SDL_HasSSE2](SDL_HasSSE2.md)
* [SDL_HasSSE3](SDL_HasSSE3.md)
* [SDL_HasSSE41](SDL_HasSSE41.md)
* [SDL_HasSSE42](SDL_HasSSE42.md)

----
[CategoryAPI](CategoryAPI.md)
