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

<<Include([SDL_CreateSemaphore](SDL_CreateSemaphore), , , from="## Begin Semaphore Example", to="## End Semaphore Example")>>

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore)

----
[CategoryAPI](CategoryAPI), [CategoryMutex](CategoryMutex)


