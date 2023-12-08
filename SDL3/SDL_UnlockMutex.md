###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UnlockMutex

Unlock the mutex.

## Syntax

```c
void SDL_UnlockMutex(SDL_Mutex *mutex) SDL_RELEASE(mutex);

```

## Function Parameters

|               |                      |
| ------------- | -------------------- |
| **mutex**     | the mutex to unlock. |

## Remarks

It is legal for the owning thread to lock an already-locked mutex. It must
unlock it the same number of times before it is actually made available for
other threads in the system (this is known as a "recursive mutex").

It is illegal to unlock a mutex that has not been locked by the current
thread, and doing so results in undefined behavior.

## Version

This function is available since SDL 3.0.0.

## Code Examples

<<Include([SDL_CreateMutex](SDL_CreateMutex.md), , , from="## Begin Mutex Example", to="## End Mutex Example")>>

----
[CategoryAPI](CategoryAPI.md), [CategoryMutex](CategoryMutex.md)
