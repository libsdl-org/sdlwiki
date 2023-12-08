###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PostSemaphore

Atomically increment a semaphore's value and wake waiting threads.

## Syntax

```c
int SDL_PostSemaphore(SDL_Semaphore *sem);

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

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore.md)
* [SDL_DestroySemaphore](SDL_DestroySemaphore.md)
* [SDL_TryWaitSemaphore](SDL_TryWaitSemaphore.md)
* [SDL_GetSemaphoreValue](SDL_GetSemaphoreValue.md)
* [SDL_WaitSemaphore](SDL_WaitSemaphore.md)
* [SDL_WaitSemaphoreTimeout](SDL_WaitSemaphoreTimeout.md)

----
[CategoryAPI](CategoryAPI.md)
