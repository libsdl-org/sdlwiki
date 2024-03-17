###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasSSE41

Determine whether the CPU has SSE4.1 features.

## Syntax

```c
SDL_bool SDL_HasSSE41(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the CPU has SSE4.1 features or
[SDL_FALSE](SDL_FALSE) if not.

## Remarks

This always returns false on CPUs that aren't using Intel instruction sets.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HasSSE](SDL_HasSSE)
* [SDL_HasSSE2](SDL_HasSSE2)
* [SDL_HasSSE3](SDL_HasSSE3)
* [SDL_HasSSE42](SDL_HasSSE42)

----
[CategoryAPI](CategoryAPI), [CategoryCPU](CategoryCPU)


