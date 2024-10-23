###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_atof

Parse a `double` from a string.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
double SDL_atof(const char *str);
```

## Function Parameters

|              |         |                                                       |
| ------------ | ------- | ----------------------------------------------------- |
| const char * | **str** | The null-terminated string to read. Must not be NULL. |

## Return Value

(double) Returns The parsed `double`.

## Remarks

The result of calling `SDL_atof(str)` is equivalent to `SDL_strtod(str,
NULL)`.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_atoi](SDL_atoi)
- [SDL_strtol](SDL_strtol)
- [SDL_strtoul](SDL_strtoul)
- [SDL_strtoll](SDL_strtoll)
- [SDL_strtoull](SDL_strtoull)
- [SDL_strtod](SDL_strtod)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

