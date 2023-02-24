###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CondWait

Wait until a condition variable is signaled.

## Syntax

```c
int SDL_CondWait(SDL_cond *cond, SDL_mutex *mutex);

```

## Function Parameters

|               |                                            |
| ------------- | ------------------------------------------ |
| **cond**      | the condition variable to wait on          |
| **mutex**     | the mutex used to coordinate thread access |

## Return Value

Returns 0 when it is signaled or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function unlocks the specified `mutex` and waits for another thread to
call [SDL_CondSignal](SDL_CondSignal)() or
[SDL_CondBroadcast](SDL_CondBroadcast)() on the condition variable `cond`.
Once the condition variable is signaled, the mutex is re-locked and the
function returns.

The mutex must be locked before calling this function. Locking the mutex
recursively (more than once) is not supported and leads to undefined
behavior.

This function is the equivalent of calling
[SDL_CondWaitTimeout](SDL_CondWaitTimeout)() with a time length of
[`SDL_MUTEX_MAXWAIT`](SDL_MUTEX_MAXWAIT).

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CondBroadcast](SDL_CondBroadcast)
* [SDL_CondSignal](SDL_CondSignal)
* [SDL_CondWaitTimeout](SDL_CondWaitTimeout)
* [SDL_CreateCond](SDL_CreateCond)
* [SDL_DestroyCond](SDL_DestroyCond)

----
[CategoryAPI](CategoryAPI), [CategoryMutex](CategoryMutex)


