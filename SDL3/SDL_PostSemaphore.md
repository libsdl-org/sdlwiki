###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PostSemaphore

Atomically increment a semaphore's value and wake waiting threads.

## Header File

Defined in [SDL_mutex.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h), but apps should use `#include <SDL3/SDL.h>`

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
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_TryWaitSemaphore](SDL_TryWaitSemaphore)
* [SDL_WaitSemaphore](SDL_WaitSemaphore)
* [SDL_WaitSemaphoreTimeout](SDL_WaitSemaphoreTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

