###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ThreadID

Get the thread identifier for the current thread.

## Syntax

```c
SDL_threadID SDL_ThreadID(void);

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

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetThreadID](SDL_GetThreadID.md)

----
[CategoryAPI](CategoryAPI.md)
