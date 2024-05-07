###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateSemaphore

Create a semaphore.

## Header File

Defined in [SDL_mutex.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mutex.h)

## Syntax

```c
SDL_sem* SDL_CreateSemaphore(Uint32 initial_value);

```

## Function Parameters

|                       |                                     |
| --------------------- | ----------------------------------- |
| **initial_value**     | the starting value of the semaphore |

## Return Value

Returns a new semaphore or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function creates a new semaphore and initializes it with the value
`initial_value`. Each wait operation on the semaphore will atomically
decrement the semaphore value and potentially block if the semaphore value
is 0. Each post operation will atomically increment the semaphore value and
wake waiting threads and allow them to retry the wait operation.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_DestroySemaphore](SDL_DestroySemaphore)
- [SDL_SemPost](SDL_SemPost)
- [SDL_SemTryWait](SDL_SemTryWait)
- [SDL_SemValue](SDL_SemValue)
- [SDL_SemWait](SDL_SemWait)
- [SDL_SemWaitTimeout](SDL_SemWaitTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

