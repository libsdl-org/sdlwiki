###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyCond

Destroy a condition variable.

## Syntax

```c
void SDL_DestroyCond(SDL_cond *cond);

```

## Function Parameters

|              |                                   |
| ------------ | --------------------------------- |
| **cond**     | the condition variable to destroy |

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CondBroadcast](SDL_CondBroadcast)
* [SDL_CondSignal](SDL_CondSignal)
* [SDL_CondWait](SDL_CondWait)
* [SDL_CondWaitTimeout](SDL_CondWaitTimeout)
* [SDL_CreateCond](SDL_CreateCond)

----
[CategoryAPI](CategoryAPI), [CategoryMutex](CategoryMutex)


