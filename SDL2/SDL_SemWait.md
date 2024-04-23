###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SemWait

Wait until a semaphore has a positive value and then decrements it.

## Header File

Defined in [SDL_mutex.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mutex.h)

## Syntax

```c
int SDL_SemWait(SDL_sem * sem);

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
[SDL_SemWaitTimeout](SDL_SemWaitTimeout)() with a time length of
[`SDL_MUTEX_MAXWAIT`](SDL_MUTEX_MAXWAIT).

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore)
* [SDL_DestroySemaphore](SDL_DestroySemaphore)
* [SDL_SemPost](SDL_SemPost)
* [SDL_SemTryWait](SDL_SemTryWait)
* [SDL_SemValue](SDL_SemValue)
* [SDL_SemWait](SDL_SemWait)
* [SDL_SemWaitTimeout](SDL_SemWaitTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


