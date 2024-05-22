###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateThread

Create a new thread with a default stack size.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
SDL_Thread * SDL_CreateThread(SDL_ThreadFunction fn, const char *name, void *data);

```

## Function Parameters

|              |                                                                                 |
| ------------ | ------------------------------------------------------------------------------- |
| **fn**       | the [SDL_ThreadFunction](SDL_ThreadFunction) function to call in the new thread |
| **name**     | the name of the thread                                                          |
| **data**     | a pointer that is passed to `fn`                                                |

## Return Value

Returns an opaque pointer to the new thread object on success, NULL if the
new thread could not be created; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

This is a convenience function, equivalent to calling
[SDL_CreateThreadWithProperties](SDL_CreateThreadWithProperties) with the
following properties set:

- [`SDL_PROP_THREAD_CREATE_ENTRY_FUNCTION_POINTER`](SDL_PROP_THREAD_CREATE_ENTRY_FUNCTION_POINTER):
  `fn`
- [`SDL_PROP_THREAD_CREATE_NAME_STRING`](SDL_PROP_THREAD_CREATE_NAME_STRING):
  `name`
- `SDL_PROP_THREAD_CREATE_USERDATA_POINTER: `data`

Note that this "function" is actually a macro that calls an internal
function with two extra parameters not listed here; they are hidden through
preprocessor macros and are needed to support various C runtimes at the
point of the function call. Language bindings that aren't using the C
headers will need to deal with this.

Usually, apps should just call this function the same way on every platform
and let the macros hide the details.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
#include <SDL3/SDL.h>

/* Very simple thread - counts 0 to 9 delaying 50ms between increments */
static int TestThread(void *ptr)
{
    int cnt;

    for (cnt = 0; cnt < 10; ++cnt) {
        SDL_Log("Thread counter: %d", cnt);
        SDL_Delay(50);
    }

    return cnt;
}

int main(int argc, char *argv[])
{
    SDL_Thread *thread;
    int         threadReturnValue;

    SDL_Log("Simple SDL_CreateThread test:");

    /* Simply create a thread */
    thread = SDL_CreateThread(TestThread, "TestThread", (void *)NULL);

    if (NULL == thread) {
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "SDL_CreateThread failed: %s", SDL_GetError());
    } else {
        SDL_WaitThread(thread, &threadReturnValue);
        SDL_Log("Thread returned value: %d", threadReturnValue);
    }

    return 0;
}

/*
 * Output:
 * Simple SDL_CreateThread test:
 * Thread counter: 0
 * Thread counter: 1
 * Thread counter: 2
 * Thread counter: 3
 * Thread counter: 4
 * Thread counter: 5
 * Thread counter: 6
 * Thread counter: 7
 * Thread counter: 8
 * Thread counter: 9
 * Thread returned value: 10
 */
```

## See Also

- [SDL_CreateThreadWithProperties](SDL_CreateThreadWithProperties)
- [SDL_WaitThread](SDL_WaitThread)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryThread](CategoryThread)

