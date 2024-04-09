###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PROP_GLOBAL_SYSTEM_DATE_FORMAT_NUMBER

Global date/time properties

## Header File

Defined in [SDL_time.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_PROP_GLOBAL_SYSTEM_DATE_FORMAT_NUMBER "SDL.time.date_format"
```

## Remarks

- [`SDL_PROP_GLOBAL_SYSTEM_DATE_FORMAT_NUMBER`](SDL_PROP_GLOBAL_SYSTEM_DATE_FORMAT_NUMBER):
  the [SDL_DATE_FORMAT](SDL_DATE_FORMAT) to use as the preferred date
  display format for the current system locale.
- [`SDL_PROP_GLOBAL_SYSTEM_TIME_FORMAT_NUMBER`](SDL_PROP_GLOBAL_SYSTEM_TIME_FORMAT_NUMBER):
  the [SDL_TIME_FORMAT](SDL_TIME_FORMAT) to use as the preferred time
  display format for the current system locale.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

