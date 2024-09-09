###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_strtoll

Parse a `long long` from a string.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
long long SDL_strtoll(const char *str, char **endp, int base);
```

## Function Parameters

|              |          |                                                                                                                                            |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| const char * | **str**  | The null-terminated string to read. Must not be NULL.                                                                                      |
| char **      | **endp** | If not NULL, the address of the first invalid character (i.e. the next character after the parsed number) will be written to this pointer. |
| int          | **base** | The base of the integer to read. The values 0, 10 and 16 are supported. If 0, the base will be inferred from the integer's prefix.         |

## Return Value

(long long) Returns The parsed `long long`.

## Remarks

This function makes fewer guarantees than the C runtime `strtoll`:

- Only the bases 10 and 16 are guaranteed to be supported. The behavior for
  other bases is unspecified.
- It is unspecified what this function returns when the parsed integer does
  not fit inside a `long long`.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_atoi](SDL_atoi)
- [SDL_atof](SDL_atof)
- [SDL_strtol](SDL_strtol)
- [SDL_strtoul](SDL_strtoul)
- [SDL_strtoull](SDL_strtoull)
- [SDL_strtod](SDL_strtod)
- [SDL_lltoa](SDL_lltoa)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

