# SDL_AsyncIOResult

Possible outcomes of an asynchronous I/O task.

## Header File

Defined in [<SDL3/SDL_asyncio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_asyncio.h)

## Syntax

```c
typedef enum SDL_AsyncIOResult
{
    SDL_ASYNCIO_COMPLETE,  /**< request was completed without error */
    SDL_ASYNCIO_FAILURE,   /**< request failed for some reason; check SDL_GetError()! */
    SDL_ASYNCIO_CANCELED   /**< request was canceled before completing. */
} SDL_AsyncIOResult;
```

## Version

This enum is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryAsyncIO](CategoryAsyncIO)

