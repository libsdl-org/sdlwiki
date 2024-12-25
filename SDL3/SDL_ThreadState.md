###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ThreadState

The SDL thread state.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
typedef enum SDL_ThreadState
{
    SDL_THREAD_STATE_ALIVE,
    SDL_THREAD_STATE_DETACHED,
    SDL_THREAD_STATE_ZOMBIE,
    SDL_THREAD_STATE_CLEANED,
} SDL_ThreadState;
```

## Remarks

SDL stores the current state of a thread in an atomic int. The current
state of a thread can be checked by calling
[SDL_GetThreadState](SDL_GetThreadState).

## Version

This enum is available since SDL 3.1.3.

## See Also

- [SDL_GetThreadState](SDL_GetThreadState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryThread](CategoryThread)

