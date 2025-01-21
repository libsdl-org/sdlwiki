###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetSemaphoreValue

Get the current value of a semaphore.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
Uint32 SDL_GetSemaphoreValue(SDL_Semaphore *sem);
```

## Function Parameters

|                                  |         |                         |
| -------------------------------- | ------- | ----------------------- |
| [SDL_Semaphore](SDL_Semaphore) * | **sem** | the semaphore to query. |

## Return Value

([Uint32](Uint32)) Returns the current value of the semaphore.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

