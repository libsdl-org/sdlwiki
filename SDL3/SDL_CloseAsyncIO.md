# SDL_CloseAsyncIO

Close and free any allocated resources for an async I/O object.

## Header File

Defined in [<SDL3/SDL_asyncio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_asyncio.h)

## Syntax

```c
bool SDL_CloseAsyncIO(SDL_AsyncIO *asyncio, bool flush, SDL_AsyncIOQueue *queue, void *userdata);
```

## Function Parameters

|                                        |              |                                                                     |
| -------------------------------------- | ------------ | ------------------------------------------------------------------- |
| [SDL_AsyncIO](SDL_AsyncIO) *           | **asyncio**  | a pointer to an [SDL_AsyncIO](SDL_AsyncIO) structure to close.      |
| bool                                   | **flush**    | true if data should sync to disk before the task completes.         |
| [SDL_AsyncIOQueue](SDL_AsyncIOQueue) * | **queue**    | a queue to add the new [SDL_AsyncIO](SDL_AsyncIO) to.               |
| void *                                 | **userdata** | an app-defined pointer that will be provided with the task results. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Closing a file is _also_ an asynchronous task! If a write failure were to
happen during the closing process, for example, the task results will
report it as usual.

Closing a file that has been written to does not guarantee the data has
made it to physical media; it may remain in the operating system's file
cache, for later writing to disk. This means that a successfully-closed
file can be lost if the system crashes or loses power in this small window.
To prevent this, call this function with the `flush` parameter set to true.
This will make the operation take longer, and perhaps increase system load
in general, but a successful result guarantees that the data has made it to
physical storage. Don't use this for temporary files, caches, and
unimportant data, and definitely use it for crucial irreplaceable files,
like game saves.

This function guarantees that the close will happen after any other pending
tasks to `asyncio`, so it's safe to open a file, start several operations,
close the file immediately, then check for all results later. This function
will not block until the tasks have completed.

Once this function returns true, `asyncio` is no longer valid, regardless
of any future outcomes. Any completed tasks might still contain this
pointer in their [SDL_AsyncIOOutcome](SDL_AsyncIOOutcome) data, in case the
app was using this value to track information, but it should not be used
again.

If this function returns false, the close wasn't started at all, and it's
safe to attempt to close again later.

An [SDL_AsyncIOQueue](SDL_AsyncIOQueue) must be specified. The
newly-created task will be added to it when it completes its work.

## Thread Safety

It is safe to call this function from any thread, but two threads should
not attempt to close the same object.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAsyncIO](CategoryAsyncIO)

