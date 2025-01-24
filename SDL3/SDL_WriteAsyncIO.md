# SDL_WriteAsyncIO

Start an async write.

## Header File

Defined in [<SDL3/SDL_asyncio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_asyncio.h)

## Syntax

```c
bool SDL_WriteAsyncIO(SDL_AsyncIO *asyncio, void *ptr, Uint64 offset, Uint64 size, SDL_AsyncIOQueue *queue, void *userdata);
```

## Function Parameters

|                                        |              |                                                                     |
| -------------------------------------- | ------------ | ------------------------------------------------------------------- |
| [SDL_AsyncIO](SDL_AsyncIO) *           | **asyncio**  | a pointer to an [SDL_AsyncIO](SDL_AsyncIO) structure.               |
| void *                                 | **ptr**      | a pointer to a buffer to write data from.                           |
| [Uint64](Uint64)                       | **offset**   | the position to start writing to the data source.                   |
| [Uint64](Uint64)                       | **size**     | the number of bytes to write to the data source.                    |
| [SDL_AsyncIOQueue](SDL_AsyncIOQueue) * | **queue**    | a queue to add the new [SDL_AsyncIO](SDL_AsyncIO) to.               |
| void *                                 | **userdata** | an app-defined pointer that will be provided with the task results. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function writes `size` bytes from `offset` position in the data source
to the area pointed at by `ptr`.

This function returns as quickly as possible; it does not wait for the
write to complete. On a successful return, this work will continue in the
background. If the work begins, even failure is asynchronous: a failing
return value from this function only means the work couldn't start at all.

`ptr` must remain available until the work is done, and may be accessed by
the system at any time until then. Do not allocate it on the stack, as this
might take longer than the life of the calling function to complete!

An [SDL_AsyncIOQueue](SDL_AsyncIOQueue) must be specified. The
newly-created task will be added to it when it completes its work.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_ReadAsyncIO](SDL_ReadAsyncIO)
- [SDL_CreateAsyncIOQueue](SDL_CreateAsyncIOQueue)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAsyncIO](CategoryAsyncIO)

