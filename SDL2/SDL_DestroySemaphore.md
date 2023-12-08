###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DestroySemaphore

Destroy a semaphore.

## Syntax

```c
void SDL_DestroySemaphore(SDL_sem * sem);

```

## Function Parameters

|             |                          |
| ----------- | ------------------------ |
| **sem**     | the semaphore to destroy |

## Remarks

It is not safe to destroy a semaphore if there are threads currently
waiting on it.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore.md)
* [SDL_SemPost](SDL_SemPost.md)
* [SDL_SemTryWait](SDL_SemTryWait.md)
* [SDL_SemValue](SDL_SemValue.md)
* [SDL_SemWait](SDL_SemWait.md)
* [SDL_SemWaitTimeout](SDL_SemWaitTimeout.md)

----
[CategoryAPI](CategoryAPI.md)
