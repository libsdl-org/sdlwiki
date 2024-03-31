###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WriteIO

Write to an [SDL_IOStream](SDL_IOStream) data stream.

## Header File

Defined in [SDL_iostream.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h), but apps should _only_ `#include <SDL3/SDL.h>`!

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
might return a positive value less than the requested write size. If the
function failed to write anything and there was an actual error, it will
return -1. For streams that support non-blocking operation, if nothing was
written because it would require blocking, this function returns -2 to
distinguish that this is not an error and the caller can try again later.

It is an error to specify a negative `size`, but this parameter is signed
so you definitely cannot overflow the return value on a successful run with
enormous amounts of data.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_IOprintf](SDL_IOprintf)
* [SDL_ReadIO](SDL_ReadIO)
* [SDL_SeekIO](SDL_SeekIO)

----
[CategoryAPI](CategoryAPI)

