###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_rand_n

Generates a pseudo-random number less than n

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
Uint32 SDL_rand_n(Uint32 n);
```

## Function Parameters

|        |       |                                |
| ------ | ----- | ------------------------------ |
| Uint32 | **n** | the number of possible values. |

## Return Value

(Uint32) Returns a random value in the range of [0 .. n-1].

## Remarks

The method used is faster and of better quality than `SDL_rand() % n`.
However just like with `SDL_rand() % n`, bias increases with larger n. Odds
are better than 99.9% even for n under 1 million.

Example: to simulate a d6 use `SDL_rand_n(6) + 1` The +1 converts 0..5 to
1..6

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

- [SDL_rand](SDL_rand)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

