###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateMutex

Create a new mutex.

## Syntax

```c
SDL_mutex* SDL_CreateMutex(void);

```

## Return Value

Returns the initialized and unlocked mutex or NULL on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

All newly-created mutexes begin in the _unlocked_ state.

Calls to [SDL_LockMutex](SDL_LockMutex.md)() will not return while the mutex
is locked by another thread. See [SDL_TryLockMutex](SDL_TryLockMutex.md)() to
attempt to lock without blocking.

SDL mutexes are reentrant.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_DestroyMutex](SDL_DestroyMutex.md)
* [SDL_LockMutex](SDL_LockMutex.md)
* [SDL_TryLockMutex](SDL_TryLockMutex.md)
* [SDL_UnlockMutex](SDL_UnlockMutex.md)

----
[CategoryAPI](CategoryAPI.md)
