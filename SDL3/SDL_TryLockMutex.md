###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_TryLockMutex

Try to lock a mutex without blocking.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
bool SDL_TryLockMutex(SDL_Mutex *mutex);
```

## Function Parameters

|                          |           |                           |
| ------------------------ | --------- | ------------------------- |
| [SDL_Mutex](SDL_Mutex) * | **mutex** | the mutex to try to lock. |

## Return Value

(bool) Returns true on success, false if the mutex would block.

## Remarks

This works just like [SDL_LockMutex](SDL_LockMutex)(), but if the mutex is
not available, this function returns false immediately.

This technique is useful if you need exclusive access to a resource but
don't want to wait for it, and will return to it to try again later.

This function returns true if passed a NULL mutex.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_LockMutex](SDL_LockMutex)
- [SDL_UnlockMutex](SDL_UnlockMutex)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

