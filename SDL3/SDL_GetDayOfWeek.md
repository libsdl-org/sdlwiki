###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetDayOfWeek

Get the day of week for a calendar date.

## Header File

Defined in [<SDL3/SDL_time.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h)

## Syntax

```c
int SDL_GetDayOfWeek(int year, int month, int day);
```

## Function Parameters

|     |           |                                  |
| --- | --------- | -------------------------------- |
| int | **year**  | the year component of the date.  |
| int | **month** | the month component of the date. |
| int | **day**   | the day component of the date.   |

## Return Value

(int) Returns a value between 0 and 6 (0 being Sunday) if the date is
valid, otherwise -1; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTime](CategoryTime)

