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

----
[CategoryAPI](CategoryAPI), [CategoryCPU](CategoryCPU)


