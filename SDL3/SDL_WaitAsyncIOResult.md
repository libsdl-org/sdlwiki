# SDL_WaitAsyncIOResult

Block until an async I/O task queue has a completed task.

## Header File

Defined in [<SDL3/SDL_asyncio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_asyncio.h)

## Syntax

```c
bool SDL_WaitAsyncIOResult(SDL_AsyncIOQueue *queue, SDL_AsyncIOOutcome *outcome, Sint32 timeoutMS);
```

## Function Parameters

|                                            |               |                                                                        |
| ------------------------------------------ | ------------- | ---------------------------------------------------------------------- |
| [SDL_AsyncIOQueue](SDL_AsyncIOQueue) *     | **queue**     | the async I/O task queue to wait on.                                   |
| [SDL_AsyncIOOutcome](SDL_AsyncIOOutcome) * | **outcome**   | details of a finished task will be written here. May not be NULL.      |
| [Sint32](Sint32)                           | **timeoutMS** | the maximum time to wait, in milliseconds, or -1 to wait indefinitely. |

## Return Value

(bool) Returns true if task has completed, false otherwise.

## Remarks

This function puts the calling thread to sleep until there a task assigned
to the queue that has finished.

If a task assigned to the queue has finished, this will return true and
fill in `outcome` with the details of the task. If no task in the queue has
finished, this function will return false.

If a task has completed, this function will free its resources and the task
pointer will no longer be valid. The task will be removed from the queue.

It is safe for multiple threads to call this function on the same queue at
once; a completed task will only go to one of the threads.

Note that by the nature of various platforms, more than one waiting thread
may wake to handle a single task, but only one will obtain it, so
`timeoutMS` is a _maximum_ wait time, and this function may return false
sooner.

This function may return false if there was a system error, the OS
inadvertently awoke multiple threads, or if
[SDL_SignalAsyncIOQueue](SDL_SignalAsyncIOQueue)() was called to wake up
all waiting threads without a finished task.

A timeout can be used to specify a maximum wait time, but rather than
polling, it is possible to have a timeout of -1 to wait forever, and use
[SDL_SignalAsyncIOQueue](SDL_SignalAsyncIOQueue)() to wake up the waiting
threads later.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SignalAsyncIOQueue](SDL_SignalAsyncIOQueue)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAsyncIO](CategoryAsyncIO)

