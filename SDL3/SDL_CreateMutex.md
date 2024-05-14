###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateMutex

Create a new mutex.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
SDL_Mutex* SDL_CreateMutex(void);

```

## Return Value

Returns the initialized and unlocked mutex or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

All newly-created mutexes begin in the _unlocked_ state.

Calls to [SDL_LockMutex](SDL_LockMutex)() will not return while the mutex
is locked by another thread. See [SDL_TryLockMutex](SDL_TryLockMutex)() to
attempt to lock without blocking.

SDL mutexes are reentrant.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
SDL_Mutex *mutex;

mutex = SDL_CreateMutex();
if (!mutex) {
  SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "Couldn't create mutex\n");
  return 1;
}

if (SDL_TryLockMutex(mutex) == 0) {
  /* Do stuff while mutex is locked */
  SDL_UnlockMutex(mutex);
} else {
  SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "Couldn't lock mutex\n");
}

SDL_DestroyMutex(mutex);
```

## See Also

- [SDL_DestroyMutex](SDL_DestroyMutex)
- [SDL_LockMutex](SDL_LockMutex)
- [SDL_TryLockMutex](SDL_TryLockMutex)
- [SDL_UnlockMutex](SDL_UnlockMutex)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

