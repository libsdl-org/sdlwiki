###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_AsyncIOTaskType

Types of asynchronous I/O tasks.

## Header File

Defined in [<SDL3/SDL_asyncio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_asyncio.h)

## Syntax

```c
typedef enum SDL_AsyncIOTaskType
{
    SDL_ASYNCIO_TASK_READ,   /**< A read operation. */
    SDL_ASYNCIO_TASK_WRITE,  /**< A write operation. */
    SDL_ASYNCIO_TASK_CLOSE   /**< A close operation. */
} SDL_AsyncIOTaskType;
```

## Version

This enum is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryAsyncIO](CategoryAsyncIO)

