###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasLSX

Determine whether the CPU has LSX (LOONGARCH SIMD) features.

## Syntax

```c
SDL_bool SDL_HasLSX(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the CPU has LOONGARCH LSX features or
[SDL_FALSE](SDL_FALSE) if not.

## Remarks

This always returns false on CPUs that aren't using LOONGARCH instruction
sets.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

