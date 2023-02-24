###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasLASX

Determine whether the CPU has LASX (LOONGARCH SIMD) features.

## Syntax

```c
SDL_bool SDL_HasLASX(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the CPU has LOONGARCH LASX features or
[SDL_FALSE](SDL_FALSE) if not.

## Remarks

This always returns false on CPUs that aren't using LOONGARCH instruction
sets.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

