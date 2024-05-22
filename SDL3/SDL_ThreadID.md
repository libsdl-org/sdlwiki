###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ThreadID

A unique numeric ID that identifies a thread.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
typedef Uint64 SDL_ThreadID;
```

## Remarks

These are different from [SDL_Thread](SDL_Thread) objects, which are
generally what an application will operate on, but having a way to uniquely
identify a thread can be useful at times.

## Version

This datatype is available since SDL 3.0.0.

## See Also

- [SDL_GetThreadID](SDL_GetThreadID)
- [SDL_GetCurrentThreadID](SDL_GetCurrentThreadID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryThread](CategoryThread)

