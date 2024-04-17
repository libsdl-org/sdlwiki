###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WriteIO

Write to an [SDL_IOStream](SDL_IOStream) data stream.

## Header File

Defined in [SDL_iostream.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
size_t SDL_WriteIO(SDL_IOStream *context, const void *ptr, size_t size);

```

## Function Parameters

|                 |                                                        |
| --------------- | ------------------------------------------------------ |
| **context**     | a pointer to an [SDL_IOStream](SDL_IOStream) structure |
| **ptr**         | a pointer to a buffer containing data to write         |
| **size**        | the number of bytes to write                           |

## Return Value

Returns the number of bytes written, which will be less than `num` on
error; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function writes exactly `size` bytes from the area pointed at by `ptr`
to the stream. If this fails for any reason, it'll return less than `size`
to demonstrate how far the write progressed. On success, it returns `num`.

On error, this function still attempts to write as much as possible, so it
might return a positive value less than the requested write size.

The caller can use [SDL_GetIOStatus](SDL_GetIOStatus)() to determine if the
problem is recoverable, such as a non-blocking write that can simply be
retried later, or a fatal error.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_IOprintf](SDL_IOprintf)
* [SDL_ReadIO](SDL_ReadIO)
* [SDL_SeekIO](SDL_SeekIO)
* [SDL_GetIOStatus](SDL_GetIOStatus)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

