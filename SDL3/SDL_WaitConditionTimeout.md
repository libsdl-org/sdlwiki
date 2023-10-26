###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WaitConditionTimeout

Wait until a condition variable is signaled or a certain time has passed.

## Syntax

```c
int SDL_WaitConditionTimeout(SDL_Condition *cond,
                        SDL_Mutex *mutex, Sint32 timeoutMS);

```

## Function Parameters

|                   |                                                                       |
| ----------------- | --------------------------------------------------------------------- |
| **cond**          | the condition variable to wait on                                     |
| **mutex**         | the mutex used to coordinate thread access                            |
| **timeoutMS**     | the maximum time to wait, in milliseconds, or -1 to wait indefinitely |

## Return Value

Returns 0 if the condition variable is signaled,
[`SDL_MUTEX_TIMEDOUT`](SDL_MUTEX_TIMEDOUT) if the condition is not signaled
in the allotted time, or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function unlocks the specified `mutex` and waits for another thread to
call [SDL_SignalCondition](SDL_SignalCondition)() or
[SDL_BroadcastCondition](SDL_BroadcastCondition)() on the condition
variable `cond`, or for the specified time to elapse. Once the condition
variable is signaled or the time elapsed, the mutex is re-locked and the
function returns.

The mutex must be locked before calling this function. Locking the mutex
recursively (more than once) is not supported and leads to undefined
behavior.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_BroadcastCondition](SDL_BroadcastCondition)
* [SDL_SignalCondition](SDL_SignalCondition)
* [SDL_WaitCondition](SDL_WaitCondition)
* [SDL_CreateCondition](SDL_CreateCondition)
* [SDL_DestroyCondition](SDL_DestroyCondition)

----
[CategoryAPI](CategoryAPI)

