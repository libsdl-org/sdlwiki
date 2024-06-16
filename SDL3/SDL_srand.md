###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_srand

Seed the pseudo-random number generator

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void SDL_srand(Uint64 seed);
```

## Function Parameters

|        |          |                                                                                                                 |
| ------ | -------- | --------------------------------------------------------------------------------------------------------------- |
| Uint64 | **seed** | the value to use as a random number seed, or 0 to use [SDL_GetPerformanceCounter](SDL_GetPerformanceCounter)(). |

## Thread Safety

This should be called on the same thread that calls [SDL_rand](SDL_rand)()

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_rand](SDL_rand)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

