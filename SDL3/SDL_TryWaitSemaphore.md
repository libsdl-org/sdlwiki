###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_TryWaitSemaphore

See if a semaphore has a positive value and decrement it if it does.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
bool SDL_TryWaitSemaphore(SDL_Semaphore *sem);
```

## Function Parameters

|                                  |         |                           |
| -------------------------------- | ------- | ------------------------- |
| [SDL_Semaphore](SDL_Semaphore) * | **sem** | the semaphore to wait on. |

## Return Value

(bool) Returns true if the wait succeeds, false if the wait would block.

## Remarks

This function checks to see if the semaphore pointed to by `sem` has a
positive value and atomically decrements the semaphore value if it does. If
the semaphore doesn't have a positive value, the function immediately
returns false.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SignalSemaphore](SDL_SignalSemaphore)
- [SDL_WaitSemaphore](SDL_WaitSemaphore)
- [SDL_WaitSemaphoreTimeout](SDL_WaitSemaphoreTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

