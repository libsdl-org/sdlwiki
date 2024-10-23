###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SignalSemaphore

Atomically increment a semaphore's value and wake waiting threads.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
void SDL_SignalSemaphore(SDL_Semaphore *sem);
```

## Function Parameters

|                                  |         |                             |
| -------------------------------- | ------- | --------------------------- |
| [SDL_Semaphore](SDL_Semaphore) * | **sem** | the semaphore to increment. |

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_TryWaitSemaphore](SDL_TryWaitSemaphore)
- [SDL_WaitSemaphore](SDL_WaitSemaphore)
- [SDL_WaitSemaphoreTimeout](SDL_WaitSemaphoreTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

