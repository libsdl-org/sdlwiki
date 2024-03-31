###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TellIO

Determine the current read/write offset in an [SDL_IOStream](SDL_IOStream) data stream.

## Header File

Defined in [SDL_iostream.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
Sint64 SDL_TellIO(SDL_IOStream *context);

```

## Function Parameters

|                 |                                                                                         |
| --------------- | --------------------------------------------------------------------------------------- |
| **context**     | an [SDL_IOStream](SDL_IOStream) data stream object from which to get the current offset |

## Return Value

Returns the current offset in the stream, or -1 if the information can not
be determined.

## Remarks

[SDL_TellIO](SDL_TellIO) is actually a wrapper function that calls the
[SDL_IOStream](SDL_IOStream)'s `seek` method, with an offset of 0 bytes
from [`SDL_IO_SEEK_CUR`](SDL_IO_SEEK_CUR), to simplify application
development.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SeekIO](SDL_SeekIO)

----
[CategoryAPI](CategoryAPI)

