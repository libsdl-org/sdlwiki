###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_TryLockMutex

Try to lock a mutex without blocking.

## Syntax

```c
int SDL_TryLockMutex(SDL_mutex * mutex) SDL_TRY_ACQUIRE(0, mutex);

```

## Function Parameters

|               |                          |
| ------------- | ------------------------ |
| **mutex**     | the mutex to try to lock |

## Return Value

Returns 0, [`SDL_MUTEX_TIMEDOUT`](SDL_MUTEX_TIMEDOUT), or -1 on error; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This works just like [SDL_LockMutex](SDL_LockMutex.md)(), but if the mutex is
not available, this function returns
[`SDL_MUTEX_TIMEOUT`](SDL_MUTEX_TIMEOUT) immediately.

This technique is useful if you need exclusive access to a resource but
don't want to wait for it, and will return to it to try again later.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateMutex](SDL_CreateMutex.md)
* [SDL_DestroyMutex](SDL_DestroyMutex.md)
* [SDL_LockMutex](SDL_LockMutex.md)
* [SDL_UnlockMutex](SDL_UnlockMutex.md)

----
[CategoryAPI](CategoryAPI.md)
