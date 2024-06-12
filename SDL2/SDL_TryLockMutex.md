###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_TryLockMutex

Try to lock a mutex without blocking.

## Header File

Defined in [SDL_mutex.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mutex.h)

## Syntax

```c
int SDL_TryLockMutex(SDL_mutex * mutex);
```

## Function Parameters

|                          |           |                          |
| ------------------------ | --------- | ------------------------ |
| [SDL_mutex](SDL_mutex) * | **mutex** | the mutex to try to lock |

## Return Value

(int) Returns 0, [`SDL_MUTEX_TIMEDOUT`](SDL_MUTEX_TIMEDOUT), or -1 on
error; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This works just like [SDL_LockMutex](SDL_LockMutex)(), but if the mutex is
not available, this function returns
[`SDL_MUTEX_TIMEOUT`](SDL_MUTEX_TIMEOUT) immediately.

This technique is useful if you need exclusive access to a resource but
don't want to wait for it, and will return to it to try again later.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateMutex](SDL_CreateMutex)
- [SDL_DestroyMutex](SDL_DestroyMutex)
- [SDL_LockMutex](SDL_LockMutex)
- [SDL_UnlockMutex](SDL_UnlockMutex)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

