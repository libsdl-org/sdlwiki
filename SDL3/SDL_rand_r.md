###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_rand_r

Get a pseudo-random number.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
Uint32 SDL_rand_r(Uint64 *state);
```

## Function Parameters

|          |           |                                                                                                                                                                                                                          |
| -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Uint64 * | **state** | a pointer to a 64-bit seed value that will be updated with each call to [SDL_rand_r](SDL_rand_r)(). If the value of the seed is 0, it will be initialized with [SDL_GetPerformanceCounter](SDL_GetPerformanceCounter)(). |

## Return Value

(Uint32) Returns a random value in the range of
[0-[SDL_MAX_UINT32](SDL_MAX_UINT32)], or 0 if state is NULL.

## Remarks

There are no guarantees as to the quality of the random sequence produced,
and this should not be used for cryptography or anything that requires good
random distribution. There are many random number libraries available with
different characteristics and you should pick one of those to meet any
serious needs.

## Thread Safety

This can be called from any thread, however each thread should pass its own
state pointer.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_rand](SDL_rand)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

