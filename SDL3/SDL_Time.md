# SDL_Time

SDL times are signed, 64-bit integers representing nanoseconds since the Unix epoch (Jan 1, 1970).

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
typedef Sint64 SDL_Time;
#define SDL_MAX_TIME SDL_MAX_SINT64
#define SDL_MIN_TIME SDL_MIN_SINT64
```

## Remarks

They can be converted between POSIX time_t values with
[SDL_NS_TO_SECONDS](SDL_NS_TO_SECONDS)() and
[SDL_SECONDS_TO_NS](SDL_SECONDS_TO_NS)(), and between Windows FILETIME
values with [SDL_TimeToWindows](SDL_TimeToWindows)() and
[SDL_TimeFromWindows](SDL_TimeFromWindows)().

## Version

This datatype is available since SDL 3.2.0.

## See Also

- [SDL_MAX_SINT64](SDL_MAX_SINT64)
- [SDL_MIN_SINT64](SDL_MIN_SINT64)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryStdinc](CategoryStdinc)

