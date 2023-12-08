###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateCond

Create a condition variable.

## Syntax

```c
SDL_cond* SDL_CreateCond(void);

```

## Return Value

Returns a new condition variable or NULL on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CondBroadcast](SDL_CondBroadcast.md)
* [SDL_CondSignal](SDL_CondSignal.md)
* [SDL_CondWait](SDL_CondWait.md)
* [SDL_CondWaitTimeout](SDL_CondWaitTimeout.md)
* [SDL_DestroyCond](SDL_DestroyCond.md)

----
[CategoryAPI](CategoryAPI.md)
