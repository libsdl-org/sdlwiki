###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_WaitThread

Wait for a thread to finish.

## Syntax

```c
void SDL_WaitThread(SDL_Thread * thread, int *status);

```

## Function Parameters

|                |                                                                                                                                              |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **thread**     | the [SDL_Thread](SDL_Thread.md) pointer that was returned from the [SDL_CreateThread](SDL_CreateThread.md)() call that started this thread         |
| **status**     | pointer to an integer that will receive the value returned from the thread function by its 'return', or NULL to not receive such value back. |

## Remarks

Threads that haven't been detached will remain (as a "zombie") until this
function cleans them up. Not doing so is a resource leak.

Once a thread has been cleaned up through this function, the
[SDL_Thread](SDL_Thread.md) that references it becomes invalid and should not
be referenced again. As such, only one thread may call
[SDL_WaitThread](SDL_WaitThread.md)() on another.

The return code for the thread function is placed in the area pointed to by
`status`, if `status` is not NULL.

You may not wait on a thread that has been used in a call to
[SDL_DetachThread](SDL_DetachThread.md)(). Use either that function or this
one, but not both, or behavior is undefined.

It is safe to pass a NULL thread to this function; it is a no-op.

Note that the thread pointer is freed by this function and is not valid
afterward.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateThread](SDL_CreateThread.md)
* [SDL_DetachThread](SDL_DetachThread.md)

----
[CategoryAPI](CategoryAPI.md)
