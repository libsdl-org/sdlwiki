# SDL_LockRWLockForWriting

Lock the read/write lock for _write_ operations.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
void SDL_LockRWLockForWriting(SDL_RWLock *rwlock);
```

## Function Parameters

|                            |            |                              |
| -------------------------- | ---------- | ---------------------------- |
| [SDL_RWLock](SDL_RWLock) * | **rwlock** | the read/write lock to lock. |

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

This function does not fail; if rwlock is NULL, it will return immediately
having locked nothing. If the rwlock is valid, this function will always
block until it can lock the mutex, and return with it locked.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_LockRWLockForReading](SDL_LockRWLockForReading)
- [SDL_TryLockRWLockForWriting](SDL_TryLockRWLockForWriting)
- [SDL_UnlockRWLock](SDL_UnlockRWLock)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

