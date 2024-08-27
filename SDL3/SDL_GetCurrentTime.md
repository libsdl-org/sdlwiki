###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCurrentTime

Gets the current value of the system realtime clock in nanoseconds since Jan 1, 1970 in Universal Coordinated Time (UTC).

## Header File

Defined in [<SDL3/SDL_time.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h)

## Syntax

```c
SDL_bool SDL_GetCurrentTime(SDL_Time *ticks);
```

## Function Parameters

|                        |           |                                                           |
| ---------------------- | --------- | --------------------------------------------------------- |
| [SDL_Time](SDL_Time) * | **ticks** | the [SDL_Time](SDL_Time) to hold the returned tick count. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTime](CategoryTime)

