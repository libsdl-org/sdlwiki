###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasSSE2

Determine whether the CPU has SSE2 features.

## Header File

Defined in [SDL_cpuinfo.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_cpuinfo.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_bool SDL_HasSSE2(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the CPU has SSE2 features or
[SDL_FALSE](SDL_FALSE) if not.

## Remarks

This always returns false on CPUs that aren't using Intel instruction sets.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HasSSE](SDL_HasSSE)
* [SDL_HasSSE3](SDL_HasSSE3)
* [SDL_HasSSE41](SDL_HasSSE41)
* [SDL_HasSSE42](SDL_HasSSE42)

----
[CategoryAPI](CategoryAPI), [CategoryCPU](CategoryCPU)


