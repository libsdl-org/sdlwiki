###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCurrentThreadID

Get the thread identifier for the current thread.

## Syntax

```c
SDL_ThreadID SDL_GetCurrentThreadID(void);

```

## Return Value

Returns the ID of the current thread.

## Remarks

This thread identifier is as reported by the underlying operating system.
If SDL is running on a platform that does not support threads the return
value will always be zero.

This function also returns a valid thread ID when called from the main
thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetThreadID](SDL_GetThreadID)

----
[CategoryAPI](CategoryAPI)

