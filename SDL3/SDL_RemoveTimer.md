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

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
extern void *my_callback_param;
extern Uint32 SDLCALL my_callbackfunc(void *userdata, SDL_TimerID timerID, Uint32 interval);

Uint32 delay = (33 / 10) * 10;  /* To round it down to the nearest 10 ms */

/* ... */

SDL_TimerID my_timer_id = SDL_AddTimer(delay, my_callbackfunc, my_callback_param);

/* ... */

SDL_RemoveTimer(my_timer_id);
```

## See Also

- [SDL_AddTimer](SDL_AddTimer)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTimer](CategoryTimer)

