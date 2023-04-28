###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LockRWLockForWriting

Lock the read/write lock for _write_ operations.

## Syntax

```c
int SDL_LockRWLockForWriting(SDL_rwlock * rwlock) SDL_ACQUIRE(rwlock);

```

## Function Parameters

|                |                             |
| -------------- | --------------------------- |
| **rwlock**     | the read/write lock to lock |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This will block until the rwlock is available, which is to say it is not
locked for reading or writing by any other thread. Only one thread may hold
the lock when it requests write access; all other threads, whether they
also want to write or only want read-only access, must wait until the
writer thread has released the lock.

It is illegal for the owning thread to lock an already-locked rwlock for
writing (read-only may be locked recursively, writing can not). Doing so
results in undefined behavior.

It is illegal to request a write lock from a thread that already holds a
read-only lock. Doing so results in undefined behavior. Unlock the
read-only lock before requesting a write lock.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_UnlockRWLock](SDL_UnlockRWLock)

----
[CategoryAPI](CategoryAPI)

