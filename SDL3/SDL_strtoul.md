# SDL_strtoul

Parse an `unsigned long` from a string.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
unsigned long SDL_strtoul(const char *str, char **endp, int base);
```

## Function Parameters

|              |          |                                                                                                                                                                                               |
| ------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| const char * | **str**  | The null-terminated string to read. Must not be NULL.                                                                                                                                         |
| char **      | **endp** | If not NULL, the address of the first invalid character (i.e. the next character after the parsed number) will be written to this pointer.                                                    |
| int          | **base** | The base of the integer to read. Supported values are 0 and 2 to 36 inclusive. If 0, the base will be inferred from the number's prefix (0x for hexadecimal, 0 for octal, decimal otherwise). |

## Return Value

(unsigned long) Returns the parsed `unsigned long`, or 0 if no number could
be parsed.

## Remarks

If `str` starts with whitespace, then those whitespace characters are
skipped before attempting to parse the number.

If the parsed number does not fit inside an `unsigned long`, the result is
clamped to the maximum representable `unsigned long` value.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_atoi](SDL_atoi)
- [SDL_atof](SDL_atof)
- [SDL_strtol](SDL_strtol)
- [SDL_strtoll](SDL_strtoll)
- [SDL_strtoull](SDL_strtoull)
- [SDL_strtod](SDL_strtod)
- [SDL_ultoa](SDL_ultoa)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

