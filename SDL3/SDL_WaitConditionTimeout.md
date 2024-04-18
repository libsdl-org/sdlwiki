###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WaitConditionTimeout

Wait until a condition variable is signaled or a certain time has passed.

## Header File

Defined in [SDL_mutex.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h), but apps should use `#include <SDL3/SDL.h>`

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

## Code Examples

```c
SDL_bool condition = SDL_FALSE;
SDL_Mutex *lock;
SDL_Condition *cond;
lock = SDL_CreateMutex();
cond = SDL_CreateCondition();

Thread_A:
    const Uint32 timeout = 1000; /* wake up every second */
    SDL_bool done = SDL_FALSE;
    while (!done) {
        SDL_LockMutex(lock);
        while (!condition && SDL_WaitConditionTimeout(cond, lock, timeout) == 0) {
            continue;
        }
        SDL_UnlockMutex(lock);
        if (condition) {
            /* ... */
        }
        /* ... do some periodic work */
    }
Thread_B:
    SDL_LockMutex(lock);
    /* ... */
    condition = SDL_TRUE;
    /* ... */
    SDL_SignalCondition(cond);
    SDL_UnlockMutex(lock);

SDL_DestroyCondition(cond);
SDL_DestroyMutex(lock);

```

## See Also

* [SDL_BroadcastCondition](SDL_BroadcastCondition)
* [SDL_SignalCondition](SDL_SignalCondition)
* [SDL_WaitCondition](SDL_WaitCondition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

