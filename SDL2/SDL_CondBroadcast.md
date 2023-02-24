###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CondBroadcast

Restart all threads that are waiting on the condition variable.

## Syntax

```c
int SDL_CondBroadcast(SDL_cond * cond);

```

## Function Parameters

|              |                                  |
| ------------ | -------------------------------- |
| **cond**     | the condition variable to signal |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CondSignal](SDL_CondSignal)
* [SDL_CondWait](SDL_CondWait)
* [SDL_CondWaitTimeout](SDL_CondWaitTimeout)
* [SDL_CreateCond](SDL_CreateCond)
* [SDL_DestroyCond](SDL_DestroyCond)

----
[CategoryAPI](CategoryAPI)

