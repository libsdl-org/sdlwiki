###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TryLockRWLockForReading

Try to lock a read/write lock _for reading_ without blocking.

## Syntax

```c
int SDL_TryLockRWLockForReading(SDL_RWLock *rwlock) SDL_TRY_ACQUIRE_SHARED(0, rwlock);

```

## Function Parameters

|                |                           |
| -------------- | ------------------------- |
| **rwlock**     | the rwlock to try to lock |

## Return Value

Returns 0, [`SDL_RWLOCK_TIMEDOUT`](SDL_RWLOCK_TIMEDOUT), or -1 on error;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This works just like
[SDL_LockRWLockForReading](SDL_LockRWLockForReading)(), but if the rwlock
is not available, then this function returns
[`SDL_RWLOCK_TIMEDOUT`](SDL_RWLOCK_TIMEDOUT) immediately.

This technique is useful if you need access to a resource but don't want to
wait for it, and will return to it to try again later.

Trying to lock for read-only access can succeed if other threads are
holding read-only locks, as this won't prevent access.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateRWLock](SDL_CreateRWLock)
* [SDL_DestroyRWLock](SDL_DestroyRWLock)
* [SDL_TryLockRWLockForReading](SDL_TryLockRWLockForReading)
* [SDL_UnlockRWLock](SDL_UnlockRWLock)

----
[CategoryAPI](CategoryAPI)

