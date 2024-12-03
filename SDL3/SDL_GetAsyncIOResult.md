###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetAsyncIOResult

Query an async I/O task queue for completed tasks.

## Header File

Defined in [<SDL3/SDL_asyncio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_asyncio.h)

## Syntax

```c
bool SDL_GetAsyncIOResult(SDL_AsyncIOQueue *queue, SDL_AsyncIOOutcome *outcome);
```

## Function Parameters

|                                            |             |                                                                   |
| ------------------------------------------ | ----------- | ----------------------------------------------------------------- |
| [SDL_AsyncIOQueue](SDL_AsyncIOQueue) *     | **queue**   | the async I/O task queue to query.                                |
| [SDL_AsyncIOOutcome](SDL_AsyncIOOutcome) * | **outcome** | details of a finished task will be written here. May not be NULL. |

## Return Value

(bool) Returns true if task has completed, false otherwise.

## Remarks

If a task assigned to this queue has finished, this will return true and
fill in `outcome` with the details of the task. If no task in the queue has
finished, this function will return false. This function does not block.

If a task has completed, this function will free its resources and the task
pointer will no longer be valid. The task will be removed from the queue.

It is safe for multiple threads to call this function on the same queue at
once; a completed task will only go to one of the threads.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_WaitAsyncIOResult](SDL_WaitAsyncIOResult)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAsyncIO](CategoryAsyncIO)

