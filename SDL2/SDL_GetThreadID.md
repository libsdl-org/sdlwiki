###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetThreadID

Get the thread identifier for the specified thread.

## Header File

Defined in [SDL_thread.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_thread.h)

## Syntax

```c
SDL_threadID SDL_GetThreadID(SDL_Thread * thread);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **thread**     | the thread to query |

## Return Value

Returns the ID of the specified thread, or the ID of the current thread if
`thread` is NULL.

## Remarks

This thread identifier is as reported by the underlying operating system.
If SDL is running on a platform that does not support threads the return
value will always be zero.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_ThreadID](SDL_ThreadID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryThread](CategoryThread)

