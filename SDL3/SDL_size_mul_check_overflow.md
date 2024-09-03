###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_size_mul_check_overflow

Multiply two integers, checking for overflow.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
SDL_FORCE_INLINE SDL_bool SDL_size_mul_check_overflow(size_t a, size_t b, size_t *ret);
```

## Function Parameters

|          |         |                                                                            |
| -------- | ------- | -------------------------------------------------------------------------- |
| size_t   | **a**   | the multiplicand.                                                          |
| size_t   | **b**   | the multiplier.                                                            |
| size_t * | **ret** | on non-overflow output, stores the multiplication result. May not be NULL. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_FALSE](SDL_FALSE) on overflow,
[SDL_TRUE](SDL_TRUE) if result is multiplied without overflow.

## Remarks

If `a * b` would overflow, return [SDL_FALSE](SDL_FALSE).

Otherwise store `a * b` via ret and return [SDL_TRUE](SDL_TRUE).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

