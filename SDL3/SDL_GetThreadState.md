###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetThreadState

Get the current state of a thread.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
SDL_ThreadState SDL_GetThreadState(SDL_Thread *thread);
```

## Function Parameters

|                            |            |                                            |
| -------------------------- | ---------- | ------------------------------------------ |
| [SDL_Thread](SDL_Thread) * | **thread** | the thread whose status you want to check. |

## Return Value

([SDL_ThreadState](SDL_ThreadState)) Returns the current state of a thread
as defined in the [SDL_ThreadState](SDL_ThreadState) enum.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_ThreadState](SDL_ThreadState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryThread](CategoryThread)

