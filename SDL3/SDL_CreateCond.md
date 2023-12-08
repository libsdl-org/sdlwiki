###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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

This function is available since SDL 3.0.0.

## Code Examples

Typical use of condition variables:

```c++
SDL_bool condition = SDL_FALSE;
SDL_mutex *lock;
SDL_cond *cond;

lock = SDL_CreateMutex();
cond = SDL_CreateCond();
.
.
Thread A:
    SDL_LockMutex(lock);
    while (!condition) {
        SDL_CondWait(cond, lock);
    }
    SDL_UnlockMutex(lock);

Thread B:
    SDL_LockMutex(lock);
    ...
    condition = SDL_TRUE;
    ...
    SDL_CondSignal(cond);
    SDL_UnlockMutex(lock);
.
.
SDL_DestroyCond(cond);
SDL_DestroyMutex(lock);
```

## Related Functions

* [SDL_CondBroadcast](SDL_CondBroadcast.md)
* [SDL_CondSignal](SDL_CondSignal.md)
* [SDL_CondWait](SDL_CondWait.md)
* [SDL_CondWaitTimeout](SDL_CondWaitTimeout.md)
* [SDL_DestroyCond](SDL_DestroyCond.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryMutex](CategoryMutex.md)
