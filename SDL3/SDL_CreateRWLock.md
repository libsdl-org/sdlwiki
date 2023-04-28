###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateRWLock

Create a new read/write lock.

## Syntax

```c
SDL_RWLock* SDL_CreateRWLock(void);

```

## Return Value

Returns the initialized and unlocked read/write lock or NULL on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

A read/write lock is useful for situations where you have multiple threads
trying to access a resource that is rarely updated. All threads requesting
a read-only lock will be allowed to run in parallel; if a thread requests a
write lock, it will be provided exclusive access. This makes it safe for
multiple threads to use a resource at the same time if they promise not to
change it, and when it has to be changed, the rwlock will serve as a
gateway to make sure those changes can be made safely.

In the right situation, a rwlock can be more efficient than a mutex, which
only lets a single thread proceed at a time, even if it won't be modifying
the data.

All newly-created read/write locks begin in the _unlocked_ state.

Calls to [SDL_LockRWLockForReading](SDL_LockRWLockForReading)() and
[SDL_LockRWLockForWriting](SDL_LockRWLockForWriting) will not return while
the rwlock is locked _for writing_ by another thread. See
[SDL_TryLockRWLockForReading](SDL_TryLockRWLockForReading)() and
[SDL_TryLockRWLockForWriting](SDL_TryLockRWLockForWriting)() to attempt to
lock without blocking.

SDL read/write locks are only recursive for read-only locks! They are not
guaranteed to be fair, or provide access in a FIFO manner! They are not
guaranteed to favor writers. You may not lock a rwlock for both read-only
and write access at the same time from the same thread (so you can't
promote your read-only lock to a write lock without unlocking first).

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_DestroyRWLock](SDL_DestroyRWLock)
* [SDL_LockRWLockForReading](SDL_LockRWLockForReading)
* [SDL_TryLockRWLockForReading](SDL_TryLockRWLockForReading)
* [SDL_LockRWLockForWriting](SDL_LockRWLockForWriting)
* [SDL_TryLockRWLockForWriting](SDL_TryLockRWLockForWriting)
* [SDL_UnlockRWLock](SDL_UnlockRWLock)

----
[CategoryAPI](CategoryAPI)

