###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetIOStatus

Query the stream status of an [SDL_IOStream](SDL_IOStream).

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
SDL_IOStatus SDL_GetIOStatus(SDL_IOStream *context);
```

## Function Parameters

|                                |             |                                            |
| ------------------------------ | ----------- | ------------------------------------------ |
| [SDL_IOStream](SDL_IOStream) * | **context** | the [SDL_IOStream](SDL_IOStream) to query. |

## Return Value

([SDL_IOStatus](SDL_IOStatus)) Returns an [SDL_IOStatus](SDL_IOStatus) enum
with the current state.

## Remarks

This information can be useful to decide if a short read or write was due
to an error, an EOF, or a non-blocking operation that isn't yet ready to
complete.

An [SDL_IOStream](SDL_IOStream)'s status is only expected to change after a
[SDL_ReadIO](SDL_ReadIO) or [SDL_WriteIO](SDL_WriteIO) call; don't expect
it to change if you just call this query function in a tight loop.

## Thread Safety

This function should not be called at the same time that another thread is
operating on the same [SDL_IOStream](SDL_IOStream).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

