# SDL_GetCurrentThreadID

Get the thread identifier for the current thread.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
SDL_ThreadID SDL_GetCurrentThreadID(void);
```

## Return Value

([SDL_ThreadID](SDL_ThreadID)) Returns the ID of the current thread.

## Remarks

This thread identifier is as reported by the underlying operating system.
If SDL is running on a platform that does not support threads the return
value will always be zero.

This function also returns a valid thread ID when called from the main
thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetThreadID](SDL_GetThreadID)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryThread](CategoryThread)

