###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_AsyncIOOutcome

Information about a completed asynchronous I/O request.

## Header File

Defined in [<SDL3/SDL_asyncio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_asyncio.h)

## Syntax

```c
typedef struct SDL_AsyncIOOutcome
{
    SDL_AsyncIO *asyncio;   /**< what generated this task. This pointer will be invalid if it was closed! */
    SDL_AsyncIOTaskType type;  /**< What sort of task was this? Read, write, etc? */
    SDL_AsyncIOResult result;  /**< the result of the work (success, failure, cancellation). */
    void *buffer;  /**< buffer where data was read/written. */
    Uint64 offset;  /**< offset in the SDL_AsyncIO where data was read/written. */
    Uint64 bytes_requested;  /**< number of bytes the task was to read/write. */
    Uint64 bytes_transferred;  /**< actual number of bytes that were read/written. */
    void *userdata;    /**< pointer provided by the app when starting the task */
} SDL_AsyncIOOutcome;
```

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryAsyncIO](CategoryAsyncIO)

