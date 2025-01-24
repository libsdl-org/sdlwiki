# SDL_TryLockRWLockForReading

Try to lock a read/write lock _for reading_ without blocking.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
bool SDL_TryLockRWLockForReading(SDL_RWLock *rwlock);
```

## Function Parameters

|                            |            |                            |
| -------------------------- | ---------- | -------------------------- |
| [SDL_RWLock](SDL_RWLock) * | **rwlock** | the rwlock to try to lock. |

## Return Value

(bool) Returns true on success, false if the lock would block.

## Remarks

This works just like
[SDL_LockRWLockForReading](SDL_LockRWLockForReading)(), but if the rwlock
is not available, then this function returns false immediately.

This technique is useful if you need access to a resource but don't want to
wait for it, and will return to it to try again later.

Trying to lock for read-only access can succeed if other threads are
holding read-only locks, as this won't prevent access.

This function returns true if passed a NULL rwlock.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_LockRWLockForReading](SDL_LockRWLockForReading)
- [SDL_TryLockRWLockForWriting](SDL_TryLockRWLockForWriting)
- [SDL_UnlockRWLock](SDL_UnlockRWLock)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

