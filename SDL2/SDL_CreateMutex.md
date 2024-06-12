###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateMutex

Create a new mutex.

## Header File

Defined in [SDL_mutex.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mutex.h)

## Syntax

```c
SDL_mutex* SDL_CreateMutex(void);
```

## Return Value

([SDL_mutex](SDL_mutex) *) Returns the initialized and unlocked mutex or
NULL on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

All newly-created mutexes begin in the _unlocked_ state.

Calls to [SDL_LockMutex](SDL_LockMutex)() will not return while the mutex
is locked by another thread. See [SDL_TryLockMutex](SDL_TryLockMutex)() to
attempt to lock without blocking.

SDL mutexes are reentrant.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_DestroyMutex](SDL_DestroyMutex)
- [SDL_LockMutex](SDL_LockMutex)
- [SDL_TryLockMutex](SDL_TryLockMutex)
- [SDL_UnlockMutex](SDL_UnlockMutex)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

