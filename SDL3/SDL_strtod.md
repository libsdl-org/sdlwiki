# SDL_strtod

Parse a `double` from a string.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
double SDL_strtod(const char *str, char **endp);
```

## Function Parameters

|              |          |                                                                                                                                            |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| const char * | **str**  | the null-terminated string to read. Must not be NULL.                                                                                      |
| char **      | **endp** | if not NULL, the address of the first invalid character (i.e. the next character after the parsed number) will be written to this pointer. |

## Return Value

(double) Returns the parsed `double`, or 0 if no number could be parsed.

## Remarks

This function makes fewer guarantees than the C runtime `strtod`:

- Only decimal notation is guaranteed to be supported. The handling of
  scientific and hexadecimal notation is unspecified.
- Whether or not INF and NAN can be parsed is unspecified.
- The precision of the result is unspecified.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_atoi](SDL_atoi)
- [SDL_atof](SDL_atof)
- [SDL_strtol](SDL_strtol)
- [SDL_strtoll](SDL_strtoll)
- [SDL_strtoul](SDL_strtoul)
- [SDL_strtoull](SDL_strtoull)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

