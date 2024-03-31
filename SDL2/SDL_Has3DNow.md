###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Has3DNow

Determine whether the CPU has 3DNow! features.

## Header File

Defined in [SDL_cpuinfo.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_cpuinfo.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_bool SDL_Has3DNow(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the CPU has 3DNow! features or
[SDL_FALSE](SDL_FALSE) if not.

## Remarks

This always returns false on CPUs that aren't using AMD instruction sets.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HasAltiVec](SDL_HasAltiVec)
* [SDL_HasAVX](SDL_HasAVX)
* [SDL_HasAVX2](SDL_HasAVX2)
* [SDL_HasMMX](SDL_HasMMX)
* [SDL_HasRDTSC](SDL_HasRDTSC)
* [SDL_HasSSE](SDL_HasSSE)
* [SDL_HasSSE2](SDL_HasSSE2)
* [SDL_HasSSE3](SDL_HasSSE3)
* [SDL_HasSSE41](SDL_HasSSE41)
* [SDL_HasSSE42](SDL_HasSSE42)

----
[CategoryAPI](CategoryAPI)

