# SDL_wcstoull

Parse an `unsigned long long` from a wide string.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
unsigned long long SDL_wcstoull(const wchar_t *str, wchar_t **endp, int base);
```

## Function Parameters

|                 |          |                                                                                                                                                                                               |
| --------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| const wchar_t * | **str**  | The null-terminated wide string to read. Must not be NULL.                                                                                                                                    |
| wchar_t **      | **endp** | If not NULL, the address of the first invalid wide character (i.e. the next character after the parsed number) will be written to this pointer.                                               |
| int             | **base** | The base of the integer to read. Supported values are 0 and 2 to 36 inclusive. If 0, the base will be inferred from the number's prefix (0x for hexadecimal, 0 for octal, decimal otherwise). |

## Return Value

(unsigned long long) Returns the parsed `unsigned long long`, or 0 if no
number could be parsed.

## Remarks

If `str` starts with whitespace, then those whitespace characters are
skipped before attempting to parse the number.

If the parsed number does not fit inside an `unsigned long long`, the
result is clamped to the minimum and maximum representable `unsigned long
long` values.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_strtoull](SDL_strtoull)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

