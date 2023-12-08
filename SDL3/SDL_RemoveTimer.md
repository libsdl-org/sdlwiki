###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RemoveTimer

Remove a timer created with [SDL_AddTimer](SDL_AddTimer.md)().

## Syntax

```c
SDL_bool SDL_RemoveTimer(SDL_TimerID id);

```

## Function Parameters

|            |                               |
| ---------- | ----------------------------- |
| **id**     | the ID of the timer to remove |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the timer is removed or
[SDL_FALSE](SDL_FALSE.md) if the timer wasn't found.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
Uint32 delay = (33 / 10) * 10;  /* To round it down to the nearest 10 ms */

/* ... */

SDL_TimerID my_timer_id = SDL_AddTimer(delay, my_callbackfunc, my_callback_param);

/* ... */

SDL_RemoveTimer(my_timer_id);
```

## Related Functions

* [SDL_AddTimer](SDL_AddTimer.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryTimer](CategoryTimer.md)
