###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LockRWLockForReading

Lock the read/write lock for _read only_ operations.

## Syntax

```c
void SDL_LockRWLockForReading(SDL_RWLock *rwlock) SDL_ACQUIRE_SHARED(rwlock);

```

## Function Parameters

|                |                             |
| -------------- | --------------------------- |
| **rwlock**     | the read/write lock to lock |

## Remarks

This will block until the rwlock is available, which is to say it is not
locked for writing by any other thread. Of all threads waiting to lock the
rwlock, all may do so at the same time as long as they are requesting
read-only access; if a thread wants to lock for writing, only one may do so
at a time, and no other threads, read-only or not, may hold the lock at the
same time.

It is legal for the owning thread to lock an already-locked rwlock for
reading. It must unlock it the same number of times before it is actually
made available for other threads in the system (this is known as a
"recursive rwlock").

Note that locking for writing is not recursive (this is only available to
read-only locks).

It is illegal to request a read-only lock from a thread that already holds
the write lock. Doing so results in undefined behavior. Unlock the write
lock before requesting a read-only lock. (But, of course, if you have the
write lock, you don't need further locks to read in any case.)

This function does not fail; if rwlock is NULL, it will return immediately
having locked nothing. If the rwlock is valid, this function will always
block until it can lock the mutex, and return with it locked.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_UnlockRWLock](SDL_UnlockRWLock)

----
[CategoryAPI](CategoryAPI)

