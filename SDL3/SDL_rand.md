###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_rand

Get a pseudo-random number.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
Uint32 SDL_rand(void);
```

## Return Value

(Uint32) Returns a random value in the range of
[0-[SDL_MAX_UINT32](SDL_MAX_UINT32)].

## Remarks

There are no guarantees as to the quality of the random sequence produced,
and this should not be used for cryptography or anything that requires good
random distribution. There are many random number libraries available with
different characteristics and you should pick one of those to meet any
serious needs.

## Thread Safety

All calls should be from from a single thread, use
[SDL_rand_r](SDL_rand_r)() when using multiple threads.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_rand_r](SDL_rand_r)
- [SDL_srand](SDL_srand)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

