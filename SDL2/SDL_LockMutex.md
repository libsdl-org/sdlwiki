###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LockMutex

Lock the mutex.

## Header File

Defined in [SDL_mutex.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mutex.h)

## Syntax

```c
int SDL_LockMutex(SDL_mutex * mutex);

#define SDL_mutexP(m)   SDL_LockMutex(m)
```

## Function Parameters

|                          |           |                    |
| ------------------------ | --------- | ------------------ |
| [SDL_mutex](SDL_mutex) * | **mutex** | the mutex to lock. |

## Return Value

(int) Return 0, or -1 on error.

## Remarks

This will block until the mutex is available, which is to say it is in the
unlocked state and the OS has chosen the caller as the next thread to lock
it. Of all threads waiting to lock the mutex, only one may do so at a time.

It is legal for the owning thread to lock an already-locked mutex. It must
unlock it the same number of times before it is actually made available for
other threads in the system (this is known as a "recursive mutex").

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

