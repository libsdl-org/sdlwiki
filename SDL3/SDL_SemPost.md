###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SemPost

Atomically increment a semaphore's value and wake waiting threads.

## Syntax

```c
int SDL_SemPost(SDL_sem *sem);

```

## Function Parameters

|             |                            |
| ----------- | -------------------------- |
| **sem**     | the semaphore to increment |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Code Examples

<<Include([SDL_CreateSemaphore](SDL_CreateSemaphore.md), , , from="## Begin Semaphore Example", to="## End Semaphore Example")>>

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore.md)
* [SDL_DestroySemaphore](SDL_DestroySemaphore.md)
* [SDL_SemTryWait](SDL_SemTryWait.md)
* [SDL_SemValue](SDL_SemValue.md)
* [SDL_SemWait](SDL_SemWait.md)
* [SDL_SemWaitTimeout](SDL_SemWaitTimeout.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryMutex](CategoryMutex.md)
