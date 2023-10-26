###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UnlockRWLock

Unlock the read/write lock.

## Syntax

```c
void SDL_UnlockRWLock(SDL_RWLock *rwlock) SDL_RELEASE_GENERIC(rwlock);

```

## Function Parameters

|                |                       |
| -------------- | --------------------- |
| **rwlock**     | the rwlock to unlock. |

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

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

