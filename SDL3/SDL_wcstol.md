###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_wcstol

Parse a `long` from a wide string.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
long SDL_wcstol(const wchar_t *str, wchar_t **endp, int base);
```

## Function Parameters

|                 |          |                                                                                                                                                                                               |
| --------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| const wchar_t * | **str**  | The null-terminated wide string to read. Must not be NULL.                                                                                                                                    |
| wchar_t **      | **endp** | If not NULL, the address of the first invalid wide character (i.e. the next character after the parsed number) will be written to this pointer.                                               |
| int             | **base** | The base of the integer to read. Supported values are 0 and 2 to 36 inclusive. If 0, the base will be inferred from the number's prefix (0x for hexadecimal, 0 for octal, decimal otherwise). |

## Return Value

(long) Returns The parsed `long`, or 0 if no number could be parsed.

## Remarks

If `str` starts with whitespace, then those whitespace characters are
skipped before attempting to parse the number.

If the parsed number does not fit inside a `long`, the result is clamped to
the minimum and maximum representable `long` values.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_strtol](SDL_strtol)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

