###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasAltiVec

Determine whether the CPU has AltiVec features.

## Syntax

```c
SDL_bool SDL_HasAltiVec(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the CPU has AltiVec features or
[SDL_FALSE](SDL_FALSE.md) if not.

## Remarks

This always returns false on CPUs that aren't using PowerPC instruction
sets.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HasAVX](SDL_HasAVX.md)
* [SDL_HasAVX2](SDL_HasAVX2.md)
* [SDL_HasAVX512F](SDL_HasAVX512F.md)
* [SDL_HasMMX](SDL_HasMMX.md)
* [SDL_HasSSE](SDL_HasSSE.md)
* [SDL_HasSSE2](SDL_HasSSE2.md)
* [SDL_HasSSE3](SDL_HasSSE3.md)
* [SDL_HasSSE41](SDL_HasSSE41.md)
* [SDL_HasSSE42](SDL_HasSSE42.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryCPU](CategoryCPU.md)
