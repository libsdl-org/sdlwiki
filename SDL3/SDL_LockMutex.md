###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LockMutex

Lock the mutex.

## Header File

Defined in [SDL_mutex.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
void SDL_LockMutex(SDL_Mutex *mutex) SDL_ACQUIRE(mutex);

```

## Function Parameters

|               |                   |
| ------------- | ----------------- |
| **mutex**     | the mutex to lock |

## Remarks

This will block until the mutex is available, which is to say it is in the
unlocked state and the OS has chosen the caller as the next thread to lock
it. Of all threads waiting to lock the mutex, only one may do so at a time.

It is legal for the owning thread to lock an already-locked mutex. It must
unlock it the same number of times before it is actually made available for
other threads in the system (this is known as a "recursive mutex").

This function does not fail; if mutex is NULL, it will return immediately
having locked nothing. If the mutex is valid, this function will always
block until it can lock the mutex, and return with it locked.

## Version

This function is available since SDL 3.0.0.

## Code Examples

<!-- # Begin Mutex Example -->
```c
int status;
SDL_mutex *mutex;

mutex = SDL_CreateMutex();
if (!mutex) {
  SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "Couldn't create mutex\n");
  return;
}

status = SDL_LockMutex(mutex);

if (status == 0) {
  SDL_Log("Locked mutex\n");
  SDL_UnlockMutex(mutex);
} else {
  SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "Couldn't lock mutex\n");
}

SDL_DestroyMutex(mutex);
```
<!-- # End Mutex Example -->

## See Also

* [SDL_TryLockMutex](SDL_TryLockMutex)
* [SDL_UnlockMutex](SDL_UnlockMutex)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)


