# SDL_DestroySemaphore

Destroy a semaphore.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
void SDL_DestroySemaphore(SDL_Semaphore *sem);
```

## Function Parameters

|                                  |         |                           |
| -------------------------------- | ------- | ------------------------- |
| [SDL_Semaphore](SDL_Semaphore) * | **sem** | the semaphore to destroy. |

## Remarks

It is not safe to destroy a semaphore if there are threads currently
waiting on it.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateSemaphore](SDL_CreateSemaphore)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

