# SDL_AddTimer

Call a callback function at a future time.

## Header File

Defined in [SDL_timer.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_timer.h)

## Syntax

```c
SDL_TimerID SDL_AddTimer(Uint32 interval,
                         SDL_TimerCallback callback,
                         void *param);
```

## Function Parameters

|                                        |              |                                                                                                    |
| -------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------- |
| [Uint32](Uint32)                       | **interval** | the timer delay, in milliseconds, passed to `callback`.                                            |
| [SDL_TimerCallback](SDL_TimerCallback) | **callback** | the [SDL_TimerCallback](SDL_TimerCallback) function to call when the specified `interval` elapses. |
| void *                                 | **param**    | a pointer that is passed to `callback`.                                                            |

## Return Value

([SDL_TimerID](SDL_TimerID)) Returns a timer ID or 0 if an error occurs;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

If you use this function, you must pass [`SDL_INIT_TIMER`](SDL_INIT_TIMER)
to [SDL_Init](SDL_Init)().

The callback function is passed the current timer interval and the user
supplied parameter from the [SDL_AddTimer](SDL_AddTimer)() call and should
return the next timer interval. If the value returned from the callback is
0, the timer is canceled.

The callback is run on a separate thread.

Timers take into account the amount of time it took to execute the
callback. For example, if the callback took 250 ms to execute and returned
1000 (ms), the timer would only wait another 750 ms before its next
iteration.

Timing may be inexact due to OS scheduling. Be sure to note the current
time with [SDL_GetTicks](SDL_GetTicks)() or
[SDL_GetPerformanceCounter](SDL_GetPerformanceCounter)() in case your
callback needs to adjust for variances.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_RemoveTimer](SDL_RemoveTimer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTimer](CategoryTimer)

