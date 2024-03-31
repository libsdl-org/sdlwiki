###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DetachThread

Let a thread clean up on exit without intervention.

## Header File

Defined in [SDL_thread.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
void SDL_DetachThread(SDL_Thread * thread);

```

## Function Parameters

|                |                                                                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **thread**     | the [SDL_Thread](SDL_Thread) pointer that was returned from the [SDL_CreateThread](SDL_CreateThread)() call that started this thread |

## Remarks

A thread may be "detached" to signify that it should not remain until
another thread has called [SDL_WaitThread](SDL_WaitThread)() on it.
Detaching a thread is useful for long-running threads that nothing needs to
synchronize with or further manage. When a detached thread is done, it
simply goes away.

There is no way to recover the return code of a detached thread. If you
need this, don't detach the thread and instead use
[SDL_WaitThread](SDL_WaitThread)().

Once a thread is detached, you should usually assume the
[SDL_Thread](SDL_Thread) isn't safe to reference again, as it will become
invalid immediately upon the detached thread's exit, instead of remaining
until someone has called [SDL_WaitThread](SDL_WaitThread)() to finally
clean it up. As such, don't detach the same thread more than once.

If a thread has already exited when passed to
[SDL_DetachThread](SDL_DetachThread)(), it will stop waiting for a call to
[SDL_WaitThread](SDL_WaitThread)() and clean up immediately. It is not safe
to detach a thread that might be used with
[SDL_WaitThread](SDL_WaitThread)().

You may not call [SDL_WaitThread](SDL_WaitThread)() on a thread that has
been detached. Use either that function or this one, but not both, or
behavior is undefined.

It is safe to pass NULL to this function; it is a no-op.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
extern int TestThread(void *ptr);
SDL_Thread *thread = SDL_CreateThread(TestThread, "TestThread", (void *)NULL);
SDL_DetachThread(thread);  /* will go away on its own upon completion. */
```

## Related Functions

* [SDL_CreateThread](SDL_CreateThread)
* [SDL_WaitThread](SDL_WaitThread)

----
[CategoryAPI](CategoryAPI), [CategoryThread](CategoryThread)


