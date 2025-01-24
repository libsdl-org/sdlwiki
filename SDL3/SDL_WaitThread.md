# SDL_WaitThread

Wait for a thread to finish.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
void SDL_WaitThread(SDL_Thread *thread, int *status);
```

## Function Parameters

|                            |            |                                                                                                                                                          |
| -------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Thread](SDL_Thread) * | **thread** | the [SDL_Thread](SDL_Thread) pointer that was returned from the [SDL_CreateThread](SDL_CreateThread)() call that started this thread.                    |
| int *                      | **status** | a pointer filled in with the value returned from the thread function by its 'return', or -1 if the thread has been detached or isn't valid, may be NULL. |

## Remarks

Threads that haven't been detached will remain until this function cleans
them up. Not doing so is a resource leak.

Once a thread has been cleaned up through this function, the
[SDL_Thread](SDL_Thread) that references it becomes invalid and should not
be referenced again. As such, only one thread may call
[SDL_WaitThread](SDL_WaitThread)() on another.

The return code from the thread function is placed in the area pointed to
by `status`, if `status` is not NULL.

You may not wait on a thread that has been used in a call to
[SDL_DetachThread](SDL_DetachThread)(). Use either that function or this
one, but not both, or behavior is undefined.

It is safe to pass a NULL thread to this function; it is a no-op.

Note that the thread pointer is freed by this function and is not valid
afterward.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateThread](SDL_CreateThread)
- [SDL_DetachThread](SDL_DetachThread)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryThread](CategoryThread)

