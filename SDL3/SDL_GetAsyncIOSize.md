###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetAsyncIOSize

Use this function to get the size of the data stream in an [SDL_AsyncIO](SDL_AsyncIO).

## Header File

Defined in [<SDL3/SDL_asyncio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_asyncio.h)

## Syntax

```c
Sint64 SDL_GetAsyncIOSize(SDL_AsyncIO *asyncio);
```

## Function Parameters

|                              |             |                                                                         |
| ---------------------------- | ----------- | ----------------------------------------------------------------------- |
| [SDL_AsyncIO](SDL_AsyncIO) * | **asyncio** | the [SDL_AsyncIO](SDL_AsyncIO) to get the size of the data stream from. |

## Return Value

([Sint64](Sint64)) Returns the size of the data stream in the
[SDL_IOStream](SDL_IOStream) on success or a negative error code on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This call is _not_ asynchronous; it assumes that obtaining this info is a
non-blocking operation in most reasonable cases.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.8.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAsyncIO](CategoryAsyncIO)

