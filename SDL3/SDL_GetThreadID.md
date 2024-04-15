###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetThreadID

Get the thread identifier for the specified thread.

## Header File

Defined in [SDL_thread.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
SDL_ThreadID SDL_GetThreadID(SDL_Thread * thread);

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

This function is available since SDL 3.0.0.

## Code Examples

```c
#include "SDL.h"

// Very simple thread - counts 0 to 9 delaying 50ms between increments
int TestThread(void *ptr)
{
    int cnt;

    for (cnt = 0; cnt < 10; ++cnt) {
        SDL_Log("\nThread counter: %d", cnt);
        SDL_Delay(50);
    }

    return cnt;
}

int main(int argc, char *argv[])
{
    SDL_Thread   *thread;
    SDL_threadID threadID;
    int          threadReturnValue;

    SDL_Log("\nSimple SDL_CreateThread test:");

    /* Simply create a thread */
    thread = SDL_CreateThread(TestThread, "TestThread", (void *)NULL);

    if (NULL == thread) {
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "\nSDL_CreateThread failed: %s\n", SDL_GetError());
        exit(-1);
    }

    /* Retrieve the ID for the newly launched thread */
    threadID = SDL_GetThreadID(thread);

    /* Wait for the thread to complete and get the return code */
    SDL_WaitThread(thread, &threadReturnValue);
    SDL_Log("\nThread returned value: %d", threadReturnValue);

    return 0;
}
```

## See Also

* [SDL_GetCurrentThreadID](SDL_GetCurrentThreadID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryThread](CategoryThread)


