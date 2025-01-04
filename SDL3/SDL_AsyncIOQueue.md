###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_AsyncIOQueue

A queue of completed asynchronous I/O tasks.

## Header File

Defined in [<SDL3/SDL_asyncio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_asyncio.h)

## Syntax

```c
typedef struct SDL_AsyncIOQueue SDL_AsyncIOQueue;
```

## Remarks

When starting an asynchronous operation, you specify a queue for the new
task. A queue can be asked later if any tasks in it have completed,
allowing an app to manage multiple pending tasks in one place, in whatever
order they complete.

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_CreateAsyncIOQueue](SDL_CreateAsyncIOQueue)
- [SDL_ReadAsyncIO](SDL_ReadAsyncIO)
- [SDL_WriteAsyncIO](SDL_WriteAsyncIO)
- [SDL_GetAsyncIOResult](SDL_GetAsyncIOResult)
- [SDL_WaitAsyncIOResult](SDL_WaitAsyncIOResult)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryAsyncIO](CategoryAsyncIO)

