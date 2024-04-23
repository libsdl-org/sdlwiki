###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ThreadPriority

The SDL thread priority.

## Header File

Defined in [SDL_thread.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_thread.h)

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

On many systems you require special privileges to set high or time critical
priority.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryEnum](CategoryEnum), [CategoryThread](CategoryThread)


