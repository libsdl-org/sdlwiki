###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_LoadFileAsync

Load all the data from a file path, asynchronously.

## Header File

Defined in [<SDL3/SDL_asyncio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_asyncio.h)

## Syntax

```c
bool SDL_LoadFileAsync(const char *file, SDL_AsyncIOQueue *queue, void *userdata);
```

## Function Parameters

|                                        |              |                                                                     |
| -------------------------------------- | ------------ | ------------------------------------------------------------------- |
| const char *                           | **file**     | the path to read all available data from.                           |
| [SDL_AsyncIOQueue](SDL_AsyncIOQueue) * | **queue**    | a queue to add the new [SDL_AsyncIO](SDL_AsyncIO) to.               |
| void *                                 | **userdata** | an app-defined pointer that will be provided with the task results. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function returns as quickly as possible; it does not wait for the read
to complete. On a successful return, this work will continue in the
background. If the work begins, even failure is asynchronous: a failing
return value from this function only means the work couldn't start at all.

The data is allocated with a zero byte at the end (null terminated) for
convenience. This extra byte is not included in
[SDL_AsyncIOOutcome](SDL_AsyncIOOutcome)'s bytes_transferred value.

This function will allocate the buffer to contain the file. It must be
deallocated by calling [SDL_free](SDL_free)() on
[SDL_AsyncIOOutcome](SDL_AsyncIOOutcome)'s buffer field after completion.

An [SDL_AsyncIOQueue](SDL_AsyncIOQueue) must be specified. The
newly-created task will be added to it when it completes its work.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_LoadFile_IO](SDL_LoadFile_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAsyncIO](CategoryAsyncIO)

