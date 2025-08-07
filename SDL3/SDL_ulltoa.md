# SDL_ulltoa

Convert an unsigned long long integer into a string.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
char * SDL_ulltoa(unsigned long long value, char *str, int radix);
```

## Function Parameters

|                    |           |                                            |
| ------------------ | --------- | ------------------------------------------ |
| unsigned long long | **value** | the unsigned long long integer to convert. |
| char *             | **str**   | the buffer to write the string into.       |
| int                | **radix** | the radix to use for string generation.    |

## Return Value

(char *) Returns `str`.

## Remarks

This requires a radix to specified for string format. Specifying 10
produces a decimal number, 16 hexadecimal, etc. Must be in the range of 2
to 36.

Note that this function will overflow a buffer if `str` is not large enough
to hold the output! It may be safer to use [SDL_snprintf](SDL_snprintf) to
clamp output, or [SDL_asprintf](SDL_asprintf) to allocate a buffer.
Otherwise, it doesn't hurt to allocate much more space than you expect to
use (and don't forget null terminator bytes, etc).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_lltoa](SDL_lltoa)
- [SDL_uitoa](SDL_uitoa)
- [SDL_ultoa](SDL_ultoa)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

