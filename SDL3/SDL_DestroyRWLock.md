###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyRWLock

Destroy a read/write lock created with [SDL_CreateRWLock](SDL_CreateRWLock)().

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
void SDL_DestroyRWLock(SDL_RWLock *rwlock);
```

## Function Parameters

|                            |            |                        |
| -------------------------- | ---------- | ---------------------- |
| [SDL_RWLock](SDL_RWLock) * | **rwlock** | the rwlock to destroy. |

## Remarks

This function must be called on any read/write lock that is no longer
needed. Failure to destroy a rwlock will result in a system memory or
resource leak. While it is safe to destroy a rwlock that is _unlocked_, it
is not safe to attempt to destroy a locked rwlock, and may result in
undefined behavior depending on the platform.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateRWLock](SDL_CreateRWLock)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

