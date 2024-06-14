###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DateTimeToTime

Converts a calendar time to an [SDL_Time](SDL_Time) in nanoseconds since the epoch.

## Header File

Defined in [<SDL3/SDL_time.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h)

## Syntax

```c
int SDL_DateTimeToTime(const SDL_DateTime *dt, SDL_Time *ticks);
```

## Function Parameters

|                                      |           |                                          |
| ------------------------------------ | --------- | ---------------------------------------- |
| const [SDL_DateTime](SDL_DateTime) * | **dt**    | the source [SDL_DateTime](SDL_DateTime). |
| [SDL_Time](SDL_Time) *               | **ticks** | the resulting [SDL_Time](SDL_Time).      |

## Return Value

(int) Returns 0 on success or -1 on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function ignores the day_of_week member of the
[SDL_DateTime](SDL_DateTime) struct, so it may remain unset.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTime](CategoryTime)

