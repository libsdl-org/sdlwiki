# SDL_DestroyAsyncIOQueue

Destroy a previously-created async I/O task queue.

## Header File

Defined in [<SDL3/SDL_asyncio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_asyncio.h)

## Syntax

```c
void SDL_DestroyAsyncIOQueue(SDL_AsyncIOQueue *queue);
```

## Function Parameters

|                                        |           |                            |
| -------------------------------------- | --------- | -------------------------- |
| [SDL_AsyncIOQueue](SDL_AsyncIOQueue) * | **queue** | the task queue to destroy. |

## Remarks

If there are still tasks pending for this queue, this call will block until
those tasks are finished. All those tasks will be deallocated. Their
results will be lost to the app.

Any pending reads from [SDL_LoadFileAsync](SDL_LoadFileAsync)() that are
still in this queue will have their buffers deallocated by this function,
to prevent a memory leak.

Once this function is called, the queue is no longer valid and should not
be used, including by other threads that might access it while destruction
is blocking on pending tasks.

Do not destroy a queue that still has threads waiting on it through
[SDL_WaitAsyncIOResult](SDL_WaitAsyncIOResult)(). You can call
[SDL_SignalAsyncIOQueue](SDL_SignalAsyncIOQueue)() first to unblock those
threads, and take measures (such as [SDL_WaitThread](SDL_WaitThread)()) to
make sure they have finished their wait and won't wait on the queue again.

## Thread Safety

It is safe to call this function from any thread, so long as no other
thread is waiting on the queue with
[SDL_WaitAsyncIOResult](SDL_WaitAsyncIOResult).

## Version

This function is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAsyncIO](CategoryAsyncIO)

