###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_WaitSemaphoreTimeout

Wait until a semaphore has a positive value and then decrements it.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
bool SDL_WaitSemaphoreTimeout(SDL_Semaphore *sem, Sint32 timeoutMS);
```

## Function Parameters

|                                  |               |                                                                         |
| -------------------------------- | ------------- | ----------------------------------------------------------------------- |
| [SDL_Semaphore](SDL_Semaphore) * | **sem**       | the semaphore to wait on.                                               |
| [Sint32](Sint32)                 | **timeoutMS** | the length of the timeout, in milliseconds, or -1 to wait indefinitely. |

## Return Value

(bool) Returns true if the wait succeeds or false if the wait times out.

## Remarks

This function suspends the calling thread until either the semaphore
pointed to by `sem` has a positive value or the specified time has elapsed.
If the call is successful it will atomically decrement the semaphore value.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_SignalSemaphore](SDL_SignalSemaphore)
- [SDL_TryWaitSemaphore](SDL_TryWaitSemaphore)
- [SDL_WaitSemaphore](SDL_WaitSemaphore)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

