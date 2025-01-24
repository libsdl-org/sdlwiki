# SDL_GetCurrentTime

Gets the current value of the system realtime clock in nanoseconds since Jan 1, 1970 in Universal Coordinated Time (UTC).

## Header File

Defined in [<SDL3/SDL_time.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h)

## Syntax

```c
bool SDL_GetCurrentTime(SDL_Time *ticks);
```

## Function Parameters

|                        |           |                                                           |
| ---------------------- | --------- | --------------------------------------------------------- |
| [SDL_Time](SDL_Time) * | **ticks** | the [SDL_Time](SDL_Time) to hold the returned tick count. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTime](CategoryTime)

