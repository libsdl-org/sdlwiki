# SDL_GetThreadState

Get the current state of a thread.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
SDL_ThreadState SDL_GetThreadState(SDL_Thread *thread);
```

## Function Parameters

|                            |            |                      |
| -------------------------- | ---------- | -------------------- |
| [SDL_Thread](SDL_Thread) * | **thread** | the thread to query. |

## Return Value

([SDL_ThreadState](SDL_ThreadState)) Returns the current state of a thread,
or [SDL_THREAD_UNKNOWN](SDL_THREAD_UNKNOWN) if the thread isn't valid.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_ThreadState](SDL_ThreadState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryThread](CategoryThread)

