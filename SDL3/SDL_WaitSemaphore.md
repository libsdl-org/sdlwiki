###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WaitSemaphore

Wait until a semaphore has a positive value and then decrements it.

## Syntax

```c
int SDL_WaitSemaphore(SDL_Semaphore *sem);

```

## Function Parameters

|             |                       |
| ----------- | --------------------- |
| **sem**     | the semaphore wait on |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function suspends the calling thread until either the semaphore
pointed to by `sem` has a positive value or the call is interrupted by a
signal or error. If the call is successful it will atomically decrement the
semaphore value.

This function is the equivalent of calling
[SDL_WaitSemaphoreTimeout](SDL_WaitSemaphoreTimeout)() with a time length
of -1.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore)
* [SDL_DestroySemaphore](SDL_DestroySemaphore)
* [SDL_PostSemaphore](SDL_PostSemaphore)
* [SDL_TryWaitSemaphore](SDL_TryWaitSemaphore)
* [SDL_GetSemaphoreValue](SDL_GetSemaphoreValue)
* [SDL_WaitSemaphore](SDL_WaitSemaphore)
* [SDL_WaitSemaphoreTimeout](SDL_WaitSemaphoreTimeout)

----
[CategoryAPI](CategoryAPI)

