###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_randf

Generate a uniform pseudo-random floating point number less than 1.0

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
float SDL_randf(void);
```

## Return Value

(float) Returns a random value in the range of [0.0, 1.0).

## Remarks

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
- [SDL_rand](SDL_rand)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

