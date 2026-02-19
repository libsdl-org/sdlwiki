# SDL_TimeToDateTime

Converts an [SDL_Time](SDL_Time) in nanoseconds since the epoch to a calendar time in the [SDL_DateTime](SDL_DateTime) format.

## Header File

Defined in [<SDL3/SDL_time.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h)

## Syntax

```c
bool SDL_TimeToDateTime(SDL_Time ticks, SDL_DateTime *dt, bool localTime);
```

## Function Parameters

|                                |               |                                                                                                                                               |
| ------------------------------ | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Time](SDL_Time)           | **ticks**     | the [SDL_Time](SDL_Time) to be converted.                                                                                                     |
| [SDL_DateTime](SDL_DateTime) * | **dt**        | the resulting [SDL_DateTime](SDL_DateTime).                                                                                                   |
| bool                           | **localTime** | the resulting [SDL_DateTime](SDL_DateTime) will be expressed in local time if true, otherwise it will be in Universal Coordinated Time (UTC). |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTime](CategoryTime)

