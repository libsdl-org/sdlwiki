###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetDaysInMonth

Get the number of days in a month for a given year.

## Header File

Defined in [SDL_time.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
int SDL_GetDaysInMonth(int year, int month);

```

## Function Parameters

|               |                  |
| ------------- | ---------------- |
| **year**      | the year         |
| **month**     | the month [1-12] |

## Return Value

Returns the number of days in the requested month, otherwise -1; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

