# SDL_GetDaysInMonth

Get the number of days in a month for a given year.

## Header File

Defined in [<SDL3/SDL_time.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h)

## Syntax

```c
int SDL_GetDaysInMonth(int year, int month);
```

## Function Parameters

|     |           |                   |
| --- | --------- | ----------------- |
| int | **year**  | the year.         |
| int | **month** | the month [1-12]. |

## Return Value

(int) Returns the number of days in the requested month or -1 on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTime](CategoryTime)

