###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateThread

Create a new thread with a default stack size.

## Syntax

```c
extern DECLSPEC SDL_Thread *SDLCALL
SDL_CreateThread(SDL_ThreadFunction fn, const char *name, void *data);

```

## Function Parameters

|              |                                                                                 |
| ------------ | ------------------------------------------------------------------------------- |
| **fn**       | the [SDL_ThreadFunction](SDL_ThreadFunction.md) function to call in the new thread |
| **name**     | the name of the thread                                                          |
| **data**     | a pointer that is passed to `fn`                                                |

## Return Value

Returns an opaque pointer to the new thread object on success, NULL if the
new thread could not be created; call [SDL_GetError](SDL_GetError.md)() for
more information.

## Remarks

This is equivalent to calling:

```c
SDL_CreateThreadWithStackSize(fn, name, 0, data);
```

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
#include "SDL.h"

/* Very simple thread - counts 0 to 9 delaying 50ms between increments */
static int TestThread(void *ptr)
{
    int cnt;

    for (cnt = 0; cnt < 10; ++cnt) {
        SDL_Log("Thread counter: %d\n", cnt);
        SDL_Delay(50);
    }

    return cnt;
}

int main(int argc, char *argv[])
{
    SDL_Thread *thread;
    int         threadReturnValue;

    SDL_Log("Simple SDL_CreateThread test:\n");

    /* Simply create a thread */
    thread = SDL_CreateThread(TestThread, "TestThread", (void *)NULL);

    if (NULL == thread) {
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "SDL_CreateThread failed: %s\n", SDL_GetError());
    } else {
        SDL_WaitThread(thread, &threadReturnValue);
        SDL_Log("Thread returned value: %d\n", threadReturnValue);
    }

    return 0;
}
```
```c
Output:
Simple SDL_CreateThread test:
Thread counter: 0
Thread counter: 1
Thread counter: 2
Thread counter: 3
Thread counter: 4
Thread counter: 5
Thread counter: 6
Thread counter: 7
Thread counter: 8
Thread counter: 9
Thread returned value: 10
```

## Related Functions

* [SDL_CreateThreadWithStackSize](SDL_CreateThreadWithStackSize.md)
* [SDL_WaitThread](SDL_WaitThread.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryThread](CategoryThread.md)
