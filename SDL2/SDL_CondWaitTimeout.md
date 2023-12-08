###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CondWaitTimeout

Wait until a condition variable is signaled or a certain time has passed.

## Syntax

```c
int SDL_CondWaitTimeout(SDL_cond * cond,
                        SDL_mutex * mutex, Uint32 ms);

```

## Function Parameters

|               |                                                                                                             |
| ------------- | ----------------------------------------------------------------------------------------------------------- |
| **cond**      | the condition variable to wait on                                                                           |
| **mutex**     | the mutex used to coordinate thread access                                                                  |
| **ms**        | the maximum time to wait, in milliseconds, or [`SDL_MUTEX_MAXWAIT`](SDL_MUTEX_MAXWAIT) to wait indefinitely |

## Return Value

Returns 0 if the condition variable is signaled,
[`SDL_MUTEX_TIMEDOUT`](SDL_MUTEX_TIMEDOUT) if the condition is not signaled
in the allotted time, or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This function unlocks the specified `mutex` and waits for another thread to
call [SDL_CondSignal](SDL_CondSignal.md)() or
[SDL_CondBroadcast](SDL_CondBroadcast.md)() on the condition variable `cond`,
or for the specified time to elapse. Once the condition variable is
signaled or the time elapsed, the mutex is re-locked and the function
returns.

The mutex must be locked before calling this function.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CondBroadcast](SDL_CondBroadcast.md)
* [SDL_CondSignal](SDL_CondSignal.md)
* [SDL_CondWait](SDL_CondWait.md)
* [SDL_CreateCond](SDL_CreateCond.md)
* [SDL_DestroyCond](SDL_DestroyCond.md)

----
[CategoryAPI](CategoryAPI.md)
