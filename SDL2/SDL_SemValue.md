###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SemValue

Get the current value of a semaphore.

## Header File

Defined in [SDL_mutex.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mutex.h)

## Syntax

```c
Uint32 SDL_SemValue(SDL_sem * sem);

```

## Function Parameters

|             |                        |
| ----------- | ---------------------- |
| **sem**     | the semaphore to query |

## Return Value

Returns the current value of the semaphore.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateSemaphore](SDL_CreateSemaphore)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

