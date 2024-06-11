###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WaitThread

Wait for a thread to finish.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
void SDL_WaitThread(SDL_Thread * thread, int *status);
```

## Function Parameters

|                |                                                                                                                                              |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **thread**     | the [SDL_Thread](SDL_Thread) pointer that was returned from the [SDL_CreateThread](SDL_CreateThread)() call that started this thread         |
| **status**     | pointer to an integer that will receive the value returned from the thread function by its 'return', or NULL to not receive such value back. |

## Remarks

Threads that haven't been detached will remain (as a "zombie") until this
function cleans them up. Not doing so is a resource leak.

Once a thread has been cleaned up through this function, the
[SDL_Thread](SDL_Thread) that references it becomes invalid and should not
be referenced again. As such, only one thread may call
[SDL_WaitThread](SDL_WaitThread)() on another.

The return code for the thread function is placed in the area pointed to by
`status`, if `status` is not NULL.

You may not wait on a thread that has been used in a call to
[SDL_DetachThread](SDL_DetachThread)(). Use either that function or this
one, but not both, or behavior is undefined.

It is safe to pass a NULL thread to this function; it is a no-op.

Note that the thread pointer is freed by this function and is not valid
afterward.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
#include <SDL3/SDL.h>

// Very simple thread - counts 0 to 9 delaying 50ms between increments
static int TestThread(void *ptr)
{
    int cnt;

    for (cnt = 0; cnt < 10; ++cnt) {
        SDL_Log("Thread counter: %d\n", cnt);
        SDL_Delay(50);
    }

    // Return the final value to the SDL_WaitThread function above
    return cnt;
}

int main(int argc, char *argv[])
{
    SDL_Thread *thread;
    int         threadReturnValue;

    SDL_Log("Simple SDL_CreateThread test:");

    // Simply create a thread
    thread = SDL_CreateThread(TestThread, "TestThread", (void *)NULL);

    if (NULL == thread) {
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "SDL_CreateThread failed: %s\n", SDL_GetError());
    } else {
        // Wait for the thread to complete. The thread functions return code will
        //       be placed in the "threadReturnValue" variable when it completes.
        //
        SDL_WaitThread(thread, &threadReturnValue);
        SDL_Log("Thread returned value: %d\n", threadReturnValue);
    }

    return 0;
}
```

## See Also

- [SDL_CreateThread](SDL_CreateThread)
- [SDL_DetachThread](SDL_DetachThread)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryThread](CategoryThread)

