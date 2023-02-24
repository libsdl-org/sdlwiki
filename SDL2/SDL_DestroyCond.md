###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DestroyCond

Destroy a condition variable.

## Syntax

```c
void SDL_DestroyCond(SDL_cond * cond);

```

## Function Parameters

|              |                                   |
| ------------ | --------------------------------- |
| **cond**     | the condition variable to destroy |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CondBroadcast](SDL_CondBroadcast)
* [SDL_CondSignal](SDL_CondSignal)
* [SDL_CondWait](SDL_CondWait)
* [SDL_CondWaitTimeout](SDL_CondWaitTimeout)
* [SDL_CreateCond](SDL_CreateCond)

----
[CategoryAPI](CategoryAPI)

