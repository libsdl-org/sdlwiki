###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_atoi

Parse an `int` from a string.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_atoi(const char *str);
```

## Function Parameters

|              |         |                                                       |
| ------------ | ------- | ----------------------------------------------------- |
| const char * | **str** | The null-terminated string to read. Must not be NULL. |

## Return Value

(int) Returns The parsed `int`.

## Remarks

The result of calling `SDL_atoi(str)` is equivalent to
`(int)SDL_strtol(str, NULL, 10)`.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_atof](SDL_atof)
- [SDL_strtol](SDL_strtol)
- [SDL_strtoul](SDL_strtoul)
- [SDL_strtoll](SDL_strtoll)
- [SDL_strtoull](SDL_strtoull)
- [SDL_strtod](SDL_strtod)
- [SDL_itoa](SDL_itoa)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

