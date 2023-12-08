###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DetachThread

Let a thread clean up on exit without intervention.

## Syntax

```c
void SDL_DetachThread(SDL_Thread * thread);

```

## Function Parameters

|                |                                                                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **thread**     | the [SDL_Thread](SDL_Thread.md) pointer that was returned from the [SDL_CreateThread](SDL_CreateThread.md)() call that started this thread |

## Remarks

A thread may be "detached" to signify that it should not remain until
another thread has called [SDL_WaitThread](SDL_WaitThread.md)() on it.
Detaching a thread is useful for long-running threads that nothing needs to
synchronize with or further manage. When a detached thread is done, it
simply goes away.

There is no way to recover the return code of a detached thread. If you
need this, don't detach the thread and instead use
[SDL_WaitThread](SDL_WaitThread.md)().

Once a thread is detached, you should usually assume the
[SDL_Thread](SDL_Thread.md) isn't safe to reference again, as it will become
invalid immediately upon the detached thread's exit, instead of remaining
until someone has called [SDL_WaitThread](SDL_WaitThread.md)() to finally
clean it up. As such, don't detach the same thread more than once.

If a thread has already exited when passed to
[SDL_DetachThread](SDL_DetachThread.md)(), it will stop waiting for a call to
[SDL_WaitThread](SDL_WaitThread.md)() and clean up immediately. It is not safe
to detach a thread that might be used with
[SDL_WaitThread](SDL_WaitThread.md)().

You may not call [SDL_WaitThread](SDL_WaitThread.md)() on a thread that has
been detached. Use either that function or this one, but not both, or
behavior is undefined.

It is safe to pass NULL to this function; it is a no-op.

## Version

This function is available since SDL 2.0.2.

## Related Functions

* [SDL_CreateThread](SDL_CreateThread.md)
* [SDL_WaitThread](SDL_WaitThread.md)

----
[CategoryAPI](CategoryAPI.md)
