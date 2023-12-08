###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroySemaphore

Destroy a semaphore.

## Syntax

```c
void SDL_DestroySemaphore(SDL_Semaphore *sem);

```

## Function Parameters

|             |                          |
| ----------- | ------------------------ |
| **sem**     | the semaphore to destroy |

## Remarks

It is not safe to destroy a semaphore if there are threads currently
waiting on it.

## Version

This function is available since SDL 3.0.0.

## Code Examples

<<Include([SDL_CreateSemaphore](SDL_CreateSemaphore.md), , , from="## Begin Semaphore Example", to="## End Semaphore Example")>>

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore.md)
* [SDL_PostSemaphore](SDL_PostSemaphore.md)
* [SDL_TryWaitSemaphore](SDL_TryWaitSemaphore.md)
* [SDL_GetSemaphoreValue](SDL_GetSemaphoreValue.md)
* [SDL_WaitSemaphore](SDL_WaitSemaphore.md)
* [SDL_WaitSemaphoreTimeout](SDL_WaitSemaphoreTimeout.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryMutex](CategoryMutex.md)
