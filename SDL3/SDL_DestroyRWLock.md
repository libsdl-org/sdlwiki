###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyRWLock

Destroy a read/write lock created with [SDL_CreateRWLock](SDL_CreateRWLock)().

## Syntax

```c
void SDL_DestroyRWLock(SDL_RWLock *rwlock);

```

## Function Parameters

|                |                       |
| -------------- | --------------------- |
| **rwlock**     | the rwlock to destroy |

## Remarks

This function must be called on any read/write lock that is no longer
needed. Failure to destroy a rwlock will result in a system memory or
resource leak. While it is safe to destroy a rwlock that is _unlocked_, it
is not safe to attempt to destroy a locked rwlock, and may result in
undefined behavior depending on the platform.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateRWLock](SDL_CreateRWLock)
* [SDL_LockRWLockForReading](SDL_LockRWLockForReading)
* [SDL_LockRWLockForWriting](SDL_LockRWLockForWriting)
* [SDL_TryLockRWLockForReading](SDL_TryLockRWLockForReading)
* [SDL_TryLockRWLockForWriting](SDL_TryLockRWLockForWriting)
* [SDL_UnlockRWLock](SDL_UnlockRWLock)

----
[CategoryAPI](CategoryAPI)

