###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_TryLockRWLockForWriting

Try to lock a read/write lock _for writing_ without blocking.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
bool SDL_TryLockRWLockForWriting(SDL_RWLock *rwlock);
```

## Function Parameters

|                            |            |                            |
| -------------------------- | ---------- | -------------------------- |
| [SDL_RWLock](SDL_RWLock) * | **rwlock** | the rwlock to try to lock. |

## Return Value

(bool) Returns true on success, false if the lock would block.

## Remarks

This works just like
[SDL_LockRWLockForWriting](SDL_LockRWLockForWriting)(), but if the rwlock
is not available, then this function returns false immediately.

This technique is useful if you need exclusive access to a resource but
don't want to wait for it, and will return to it to try again later.

It is illegal for the owning thread to lock an already-locked rwlock for
writing (read-only may be locked recursively, writing can not). Doing so
results in undefined behavior.

It is illegal to request a write lock from a thread that already holds a
read-only lock. Doing so results in undefined behavior. Unlock the
read-only lock before requesting a write lock.

This function returns true if passed a NULL rwlock.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_LockRWLockForWriting](SDL_LockRWLockForWriting)
- [SDL_TryLockRWLockForReading](SDL_TryLockRWLockForReading)
- [SDL_UnlockRWLock](SDL_UnlockRWLock)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

