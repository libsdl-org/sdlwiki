###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SignalAsyncIOQueue

Wake up any threads that are blocking in [SDL_WaitAsyncIOResult](SDL_WaitAsyncIOResult)().

## Header File

Defined in [<SDL3/SDL_asyncio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_asyncio.h)

## Syntax

```c
void SDL_SignalAsyncIOQueue(SDL_AsyncIOQueue *queue);
```

## Function Parameters

|                                        |           |                                     |
| -------------------------------------- | --------- | ----------------------------------- |
| [SDL_AsyncIOQueue](SDL_AsyncIOQueue) * | **queue** | the async I/O task queue to signal. |

## Remarks

This will unblock any threads that are sleeping in a call to
[SDL_WaitAsyncIOResult](SDL_WaitAsyncIOResult) for the specified queue, and
cause them to return from that function.

This can be useful when destroying a queue to make sure nothing is touching
it indefinitely. In this case, once this call completes, the caller should
take measures to make sure any previously-blocked threads have returned
from their wait and will not touch the queue again (perhaps by setting a
flag to tell the threads to terminate and then using
[SDL_WaitThread](SDL_WaitThread)() to make sure they've done so).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.8.

## See Also

- [SDL_WaitAsyncIOResult](SDL_WaitAsyncIOResult)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAsyncIO](CategoryAsyncIO)

