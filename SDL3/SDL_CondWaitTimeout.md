###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CondWaitTimeout

Wait until a condition variable is signaled or a certain time has passed.

## Syntax

```c
int SDL_CondWaitTimeout(SDL_cond *cond,
                        SDL_mutex *mutex, Sint32 timeoutMS);

```

## Function Parameters

|                   |                                                                                                             |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| **cond**          | the condition variable to wait on                                                                           |
| **mutex**         | the mutex used to coordinate thread access                                                                  |
| **timeoutMS**     | the maximum time to wait, in milliseconds, or [`SDL_MUTEX_MAXWAIT`](SDL_MUTEX_MAXWAIT) to wait indefinitely |

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

The mutex must be locked before calling this function. Locking the mutex
recursively (more than once) is not supported and leads to undefined
behavior.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
SDL_bool condition = SDL_FALSE;
SDL_mutex *lock;
SDL_cond *cond;

lock = SDL_CreateMutex();
cond = SDL_CreateCond();
.
.
Thread A:
    const Uint32 timeout = 1000; /* wake up every second */

    while (!done) {
        SDL_LockMutex(lock);
        while (!condition && SDL_CondWaitTimeout(cond, lock, timeout) == 0) {
            continue;
        }
        SDL_UnlockMutex(lock);

        if (condition) {
            ...
        }

        ... do some periodic work
    }

Thread B:
    SDL_LockMutex(lock);
    ...
    condition = SDL_TRUE;
    ...
    SDL_CondSignal(cond);
    SDL_UnlockMutex(lock);
.
.
SDL_DestroyCond(cond);
SDL_DestroyMutex(lock);
```

## Related Functions

* [SDL_CondBroadcast](SDL_CondBroadcast.md)
* [SDL_CondSignal](SDL_CondSignal.md)
* [SDL_CondWait](SDL_CondWait.md)
* [SDL_CreateCond](SDL_CreateCond.md)
* [SDL_DestroyCond](SDL_DestroyCond.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryMutex](CategoryMutex.md)
