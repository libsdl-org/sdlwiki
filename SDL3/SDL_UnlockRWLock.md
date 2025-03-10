# SDL_UnlockRWLock

Unlock the read/write lock.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
void SDL_UnlockRWLock(SDL_RWLock *rwlock);
```

## Function Parameters

|                            |            |                       |
| -------------------------- | ---------- | --------------------- |
| [SDL_RWLock](SDL_RWLock) * | **rwlock** | the rwlock to unlock. |

## Remarks

Use this function to unlock the rwlock, whether it was locked for read-only
or write operations.

It is legal for the owning thread to lock an already-locked read-only lock.
It must unlock it the same number of times before it is actually made
available for other threads in the system (this is known as a "recursive
rwlock").

It is illegal to unlock a rwlock that has not been locked by the current
thread, and doing so results in undefined behavior.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_LockRWLockForReading](SDL_LockRWLockForReading)
- [SDL_LockRWLockForWriting](SDL_LockRWLockForWriting)
- [SDL_TryLockRWLockForReading](SDL_TryLockRWLockForReading)
- [SDL_TryLockRWLockForWriting](SDL_TryLockRWLockForWriting)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

