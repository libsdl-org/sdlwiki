###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MAX_TIME

SDL times are signed, 64-bit integers representing nanoseconds since the Unix epoch (Jan 1, 1970).

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_MAX_TIME SDL_MAX_SINT64
```

## Remarks

They can be converted between POSIX time_t values with
[SDL_NS_TO_SECONDS](SDL_NS_TO_SECONDS)() and
[SDL_SECONDS_TO_NS](SDL_SECONDS_TO_NS)(), and between Windows FILETIME
values with [SDL_TimeToWindows](SDL_TimeToWindows)() and
[SDL_TimeFromWindows](SDL_TimeFromWindows)().

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

