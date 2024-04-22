###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SemPost

Atomically increment a semaphore's value and wake waiting threads.

## Header File

Defined in [SDL_mutex.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mutex.h)

## Syntax

```c
int SDL_SemPost(SDL_sem * sem);

```

## Function Parameters

|             |                            |
| ----------- | -------------------------- |
| **sem**     | the semaphore to increment |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_CreateSemaphore](SDL_CreateSemaphore)
* [SDL_DestroySemaphore](SDL_DestroySemaphore)
* [SDL_SemTryWait](SDL_SemTryWait)
* [SDL_SemValue](SDL_SemValue)
* [SDL_SemWait](SDL_SemWait)
* [SDL_SemWaitTimeout](SDL_SemWaitTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

