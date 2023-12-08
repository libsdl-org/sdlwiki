###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SemTryWait

See if a semaphore has a positive value and decrement it if it does.

## Syntax

```c
int SDL_SemTryWait(SDL_sem * sem);

```

## Function Parameters

|             |                          |
| ----------- | ------------------------ |
| **sem**     | the semaphore to wait on |

## Return Value

Returns 0 if the wait succeeds, [`SDL_MUTEX_TIMEDOUT`](SDL_MUTEX_TIMEDOUT)
if the wait would block, or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This function checks to see if the semaphore pointed to by `sem` has a
positive value and atomically decrements the semaphore value if it does. If
the semaphore doesn't have a positive value, the function immediately
returns [SDL_MUTEX_TIMEDOUT](SDL_MUTEX_TIMEDOUT.md).

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore.md)
* [SDL_DestroySemaphore](SDL_DestroySemaphore.md)
* [SDL_SemPost](SDL_SemPost.md)
* [SDL_SemValue](SDL_SemValue.md)
* [SDL_SemWait](SDL_SemWait.md)
* [SDL_SemWaitTimeout](SDL_SemWaitTimeout.md)

----
[CategoryAPI](CategoryAPI.md)
