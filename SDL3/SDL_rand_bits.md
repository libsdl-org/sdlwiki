###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_rand_bits

Generates 32 pseudo-random bits.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
Uint32 SDL_rand_bits(void);
```

## Return Value

(Uint32) Returns a random value in the range of
[0-[SDL_MAX_UINT32](SDL_MAX_UINT32)].

## Remarks

You likely want to use [SDL_rand_n](SDL_rand_n)() to get a psuedo-randum
number instead.

If you want reproducible output, be sure to initialize with
[SDL_srand](SDL_srand)() first.

There are no guarantees as to the quality of the random sequence produced,
and this should not be used for security (cryptography, passwords) or where
money is on the line (loot-boxes, casinos). There are many random number
libraries available with different characteristics and you should pick one
of those to meet any serious needs.

## Thread Safety

All calls should be made from a single thread

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_srand](SDL_srand)
- [SDL_rand_n](SDL_rand_n)
- [SDL_rand_float](SDL_rand_float)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

