###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_size_add_overflow

Add two integers, checking for overflow.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
SDL_FORCE_INLINE int SDL_size_add_overflow (size_t a, size_t b, size_t *ret);
```

## Function Parameters

|          |         |                                                                      |
| -------- | ------- | -------------------------------------------------------------------- |
| size_t   | **a**   | the first addend.                                                    |
| size_t   | **b**   | the second addend.                                                   |
| size_t * | **ret** | on non-overflow output, stores the addition result. May not be NULL. |

## Return Value

(int) Returns -1 on overflow, 0 if result doesn't overflow.

## Remarks

If `a + b` would overflow, return -1.

Otherwise store `a + b` via ret and return 0.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

