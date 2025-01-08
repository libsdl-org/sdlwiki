###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_CreateAsyncIOQueue

Create a task queue for tracking multiple I/O operations.

## Header File

Defined in [<SDL3/SDL_asyncio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_asyncio.h)

## Syntax

```c
SDL_AsyncIOQueue * SDL_CreateAsyncIOQueue(void);
```

## Return Value

([SDL_AsyncIOQueue](SDL_AsyncIOQueue) *) Returns a new task queue object or
NULL if there was an error; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

Async I/O operations are assigned to a queue when started. The queue can be
checked for completed tasks thereafter.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.8.

## See Also

- [SDL_DestroyAsyncIOQueue](SDL_DestroyAsyncIOQueue)
- [SDL_GetAsyncIOResult](SDL_GetAsyncIOResult)
- [SDL_WaitAsyncIOResult](SDL_WaitAsyncIOResult)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAsyncIO](CategoryAsyncIO)

