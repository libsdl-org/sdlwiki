# SDL_srand

Seeds the pseudo-random number generator.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void SDL_srand(Uint64 seed);
```

## Function Parameters

|                  |          |                                                                                                                 |
| ---------------- | -------- | --------------------------------------------------------------------------------------------------------------- |
| [Uint64](Uint64) | **seed** | the value to use as a random number seed, or 0 to use [SDL_GetPerformanceCounter](SDL_GetPerformanceCounter)(). |

## Remarks

Reusing the seed number will cause [SDL_rand_](SDL_rand_)*() to repeat the
same stream of 'random' numbers.

## Thread Safety

This should be called on the same thread that calls [SDL_rand](SDL_rand)*()

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_rand](SDL_rand)
- [SDL_rand_bits](SDL_rand_bits)
- [SDL_randf](SDL_randf)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

