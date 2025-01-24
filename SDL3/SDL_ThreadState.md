# SDL_ThreadState

The SDL thread state.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
typedef enum SDL_ThreadState
{
    SDL_THREAD_UNKNOWN,     /**< The thread is not valid */
    SDL_THREAD_ALIVE,       /**< The thread is currently running */
    SDL_THREAD_DETACHED,    /**< The thread is detached and can't be waited on */
    SDL_THREAD_COMPLETE     /**< The thread has finished and should be cleaned up with SDL_WaitThread() */
} SDL_ThreadState;
```

## Remarks

The current state of a thread can be checked by calling
[SDL_GetThreadState](SDL_GetThreadState).

## Version

This enum is available since SDL 3.2.0.

## See Also

- [SDL_GetThreadState](SDL_GetThreadState)






----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryThread](CategoryThread)

