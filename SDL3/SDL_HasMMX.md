###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasMMX

Determine whether the CPU has MMX features.

## Syntax

```c
SDL_bool SDL_HasMMX(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the CPU has MMX features or
[SDL_FALSE](SDL_FALSE) if not.

## Remarks

This always returns false on CPUs that aren't using Intel instruction sets.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HasAltiVec](SDL_HasAltiVec)
* [SDL_HasAVX](SDL_HasAVX)
* [SDL_HasAVX2](SDL_HasAVX2)
* [SDL_HasRDTSC](SDL_HasRDTSC)
* [SDL_HasSSE](SDL_HasSSE)
* [SDL_HasSSE2](SDL_HasSSE2)
* [SDL_HasSSE3](SDL_HasSSE3)
* [SDL_HasSSE41](SDL_HasSSE41)
* [SDL_HasSSE42](SDL_HasSSE42)

----
[CategoryAPI](CategoryAPI), [CategoryCPU](CategoryCPU)


