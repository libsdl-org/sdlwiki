###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TimeToDateTime

Converts an [SDL_Time](SDL_Time) in nanoseconds since the epoch to a calendar time in the [SDL_DateTime](SDL_DateTime) format.

## Header File

Defined in [<SDL3/SDL_time.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h)

## Syntax

```c
int SDL_TimeToDateTime(SDL_Time ticks, SDL_DateTime *dt, SDL_bool localTime);
```

## Function Parameters

|                   |                                                                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **ticks**         | the [SDL_Time](SDL_Time) to be converted                                                                                                     |
| **dt**            | the resulting [SDL_DateTime](SDL_DateTime)                                                                                                   |
| **localTime**     | the resulting [SDL_DateTime](SDL_DateTime) will be expressed in local time if true, otherwise it will be in Universal Coordinated Time (UTC) |

## Return Value

Returns 0 on success or -1 on error; call [SDL_GetError](SDL_GetError)()
for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTime](CategoryTime)

