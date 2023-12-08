###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SemWaitTimeout

Wait until a semaphore has a positive value and then decrements it.

## Syntax

```c
int SDL_SemWaitTimeout(SDL_sem *sem, Uint32 timeout);

```

## Function Parameters

|                 |                                            |
| --------------- | ------------------------------------------ |
| **sem**         | the semaphore to wait on                   |
| **timeout**     | the length of the timeout, in milliseconds |

## Return Value

Returns 0 if the wait succeeds, [`SDL_MUTEX_TIMEDOUT`](SDL_MUTEX_TIMEDOUT)
if the wait does not succeed in the allotted time, or a negative error code
on failure; call [SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This function suspends the calling thread until either the semaphore
pointed to by `sem` has a positive value, the call is interrupted by a
signal or error, or the specified time has elapsed. If the call is
successful it will atomically decrement the semaphore value.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore.md)
* [SDL_DestroySemaphore](SDL_DestroySemaphore.md)
* [SDL_SemPost](SDL_SemPost.md)
* [SDL_SemTryWait](SDL_SemTryWait.md)
* [SDL_SemValue](SDL_SemValue.md)
* [SDL_SemWait](SDL_SemWait.md)

----
[CategoryAPI](CategoryAPI.md)
