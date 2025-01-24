# SDL_RemoveTimer

Remove a timer created with [SDL_AddTimer](SDL_AddTimer)().

## Header File

Defined in [SDL_timer.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_timer.h)

## Syntax

```c
SDL_bool SDL_RemoveTimer(SDL_TimerID id);
```

## Function Parameters

|                            |        |                                |
| -------------------------- | ------ | ------------------------------ |
| [SDL_TimerID](SDL_TimerID) | **id** | the ID of the timer to remove. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the timer is removed
or [SDL_FALSE](SDL_FALSE) if the timer wasn't found.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_AddTimer](SDL_AddTimer)


## (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTimer](CategoryTimer)

