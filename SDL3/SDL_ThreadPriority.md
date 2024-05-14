###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ThreadPriority

The SDL thread priority.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
typedef enum SDL_ThreadPriority {
    SDL_THREAD_PRIORITY_LOW,
    SDL_THREAD_PRIORITY_NORMAL,
    SDL_THREAD_PRIORITY_HIGH,
    SDL_THREAD_PRIORITY_TIME_CRITICAL
} SDL_ThreadPriority;
```

## Remarks

SDL will make system changes as necessary in order to apply the thread
priority. Code which attempts to control thread state related to priority
should be aware that calling [SDL_SetThreadPriority](SDL_SetThreadPriority)
may alter such state.
[SDL_HINT_THREAD_PRIORITY_POLICY](SDL_HINT_THREAD_PRIORITY_POLICY) can be
used to control aspects of this behavior.

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryThread](CategoryThread)

