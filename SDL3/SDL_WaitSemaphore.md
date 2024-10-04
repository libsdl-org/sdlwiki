###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_WaitSemaphore

Wait until a semaphore has a positive value and then decrements it.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
void SDL_WaitSemaphore(SDL_Semaphore *sem);
```

## Function Parameters

|                                  |         |                        |
| -------------------------------- | ------- | ---------------------- |
| [SDL_Semaphore](SDL_Semaphore) * | **sem** | the semaphore wait on. |

## Remarks

This function suspends the calling thread until the semaphore pointed to by
`sem` has a positive value, and then atomically decrement the semaphore
value.

This function is the equivalent of calling
[SDL_WaitSemaphoreTimeout](SDL_WaitSemaphoreTimeout)() with a time length
of -1.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SignalSemaphore](SDL_SignalSemaphore)
- [SDL_TryWaitSemaphore](SDL_TryWaitSemaphore)
- [SDL_WaitSemaphoreTimeout](SDL_WaitSemaphoreTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

