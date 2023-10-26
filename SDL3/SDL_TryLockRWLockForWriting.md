###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TryLockRWLockForWriting

Try to lock a read/write lock _for writing_ without blocking.

## Syntax

```c
int SDL_TryLockRWLockForWriting(SDL_RWLock *rwlock) SDL_TRY_ACQUIRE(0, rwlock);

```

## Function Parameters

|                |                           |
| -------------- | ------------------------- |
| **rwlock**     | the rwlock to try to lock |

## Return Value

Returns 0 or [`SDL_RWLOCK_TIMEDOUT`](SDL_RWLOCK_TIMEDOUT)

## Remarks

This works just like
[SDL_LockRWLockForWriting](SDL_LockRWLockForWriting)(), but if the rwlock
is not available, this function returns
[`SDL_RWLOCK_TIMEDOUT`](SDL_RWLOCK_TIMEDOUT) immediately.

This technique is useful if you need exclusive access to a resource but
don't want to wait for it, and will return to it to try again later.

It is illegal for the owning thread to lock an already-locked rwlock for
writing (read-only may be locked recursively, writing can not). Doing so
results in undefined behavior.

It is illegal to request a write lock from a thread that already holds a
read-only lock. Doing so results in undefined behavior. Unlock the
read-only lock before requesting a write lock.

This function does not fail; if rwlock is NULL, it will return 0
immediately having locked nothing. If rwlock is valid, this function will
always either lock the rwlock and return 0, or return
[SDL_RWLOCK_TIMEOUT](SDL_RWLOCK_TIMEOUT) and lock nothing.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateRWLock](SDL_CreateRWLock)
* [SDL_DestroyRWLock](SDL_DestroyRWLock)
* [SDL_TryLockRWLockForWriting](SDL_TryLockRWLockForWriting)
* [SDL_UnlockRWLock](SDL_UnlockRWLock)

----
[CategoryAPI](CategoryAPI)

