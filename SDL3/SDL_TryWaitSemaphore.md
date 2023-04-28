###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TryWaitSemaphore

See if a semaphore has a positive value and decrement it if it does.

## Syntax

```c
int SDL_TryWaitSemaphore(SDL_Semaphore *sem);

```

## Function Parameters

|             |                          |
| ----------- | ------------------------ |
| **sem**     | the semaphore to wait on |

## Return Value

Returns 0 if the wait succeeds, [`SDL_MUTEX_TIMEDOUT`](SDL_MUTEX_TIMEDOUT)
if the wait would block, or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function checks to see if the semaphore pointed to by `sem` has a
positive value and atomically decrements the semaphore value if it does. If
the semaphore doesn't have a positive value, the function immediately
returns [SDL_MUTEX_TIMEDOUT](SDL_MUTEX_TIMEDOUT).

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore)
* [SDL_DestroySemaphore](SDL_DestroySemaphore)
* [SDL_PostSemaphore](SDL_PostSemaphore)
* [SDL_GetSemaphoreValue](SDL_GetSemaphoreValue)
* [SDL_WaitSemaphore](SDL_WaitSemaphore)
* [SDL_WaitSemaphoreTimeout](SDL_WaitSemaphoreTimeout)

----
[CategoryAPI](CategoryAPI)

