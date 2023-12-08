###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyMutex

Destroy a mutex created with [SDL_CreateMutex](SDL_CreateMutex.md)().

## Syntax

```c
void SDL_DestroyMutex(SDL_Mutex *mutex);

```

## Function Parameters

|               |                      |
| ------------- | -------------------- |
| **mutex**     | the mutex to destroy |

## Remarks

This function must be called on any mutex that is no longer needed. Failure
to destroy a mutex will result in a system memory or resource leak. While
it is safe to destroy a mutex that is _unlocked_, it is not safe to attempt
to destroy a locked mutex, and may result in undefined behavior depending
on the platform.

## Version

This function is available since SDL 3.0.0.

## Code Examples

<<Include([SDL_CreateMutex](SDL_CreateMutex.md), , , from="## Begin Mutex Example", to="## End Mutex Example")>>

## Related Functions

* [SDL_CreateMutex](SDL_CreateMutex.md)
* [SDL_LockMutex](SDL_LockMutex.md)
* [SDL_TryLockMutex](SDL_TryLockMutex.md)
* [SDL_UnlockMutex](SDL_UnlockMutex.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryMutex](CategoryMutex.md)
