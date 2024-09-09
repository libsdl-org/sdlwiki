###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_wcstol

Parse a `long` from a wide string.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
long SDL_wcstol(const wchar_t *str, wchar_t **endp, int base);
```

## Function Parameters

|                 |          |                                                                                                                                                 |
| --------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| const wchar_t * | **str**  | The null-terminated wide string to read. Must not be NULL.                                                                                      |
| wchar_t **      | **endp** | If not NULL, the address of the first invalid wide character (i.e. the next character after the parsed number) will be written to this pointer. |
| int             | **base** | The base of the integer to read. The values 0, 10 and 16 are supported. If 0, the base will be inferred from the integer's prefix.              |

## Return Value

(long) Returns The parsed `long`.

## Remarks

This function makes fewer guarantees than the C runtime `wcstol`:

- Only the bases 10 and 16 are guaranteed to be supported. The behavior for
  other bases is unspecified.
- It is unspecified what this function returns when the parsed integer does
  not fit inside a `long`.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_strtol](SDL_strtol)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

