###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSemaphoreValue

Get the current value of a semaphore.

## Syntax

```c
Uint32 SDL_GetSemaphoreValue(SDL_Semaphore *sem);

```

## Function Parameters

|             |                        |
| ----------- | ---------------------- |
| **sem**     | the semaphore to query |

## Return Value

Returns the current value of the semaphore.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore)

----
[CategoryAPI](CategoryAPI)

