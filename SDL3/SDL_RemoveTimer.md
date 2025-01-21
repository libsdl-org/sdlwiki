###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_RemoveTimer

Remove a timer created with [SDL_AddTimer](SDL_AddTimer)().

## Header File

Defined in [<SDL3/SDL_timer.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_timer.h)

## Syntax

```c
bool SDL_RemoveTimer(SDL_TimerID id);
```

## Function Parameters

|                            |        |                                |
| -------------------------- | ------ | ------------------------------ |
| [SDL_TimerID](SDL_TimerID) | **id** | the ID of the timer to remove. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_AddTimer](SDL_AddTimer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTimer](CategoryTimer)

