###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WaitSemaphoreTimeout

Wait until a semaphore has a positive value and then decrements it.

## Syntax

```c
int SDL_WaitSemaphoreTimeout(SDL_Semaphore *sem, Sint32 timeoutMS);

```

## Function Parameters

|                   |                                            |
| ----------------- | ------------------------------------------ |
| **sem**           | the semaphore to wait on                   |
| **timeoutMS**     | the length of the timeout, in milliseconds |

## Return Value

Returns 0 if the wait succeeds, [`SDL_MUTEX_TIMEDOUT`](SDL_MUTEX_TIMEDOUT)
if the wait does not succeed in the allotted time, or a negative error code
on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function suspends the calling thread until either the semaphore
pointed to by `sem` has a positive value, the call is interrupted by a
signal or error, or the specified time has elapsed. If the call is
successful it will atomically decrement the semaphore value.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore)
* [SDL_DestroySemaphore](SDL_DestroySemaphore)
* [SDL_PostSemaphore](SDL_PostSemaphore)
* [SDL_TryWaitSemaphore](SDL_TryWaitSemaphore)
* [SDL_GetSemaphoreValue](SDL_GetSemaphoreValue)
* [SDL_WaitSemaphore](SDL_WaitSemaphore)

----
[CategoryAPI](CategoryAPI)

