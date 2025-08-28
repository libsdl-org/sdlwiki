# SDL_TellIO

Determine the current read/write offset in an [SDL_IOStream](SDL_IOStream) data stream.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
Sint64 SDL_TellIO(SDL_IOStream *context);
```

## Function Parameters

|                                |             |                                                                                          |
| ------------------------------ | ----------- | ---------------------------------------------------------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **context** | an [SDL_IOStream](SDL_IOStream) data stream object from which to get the current offset. |

## Return Value

([Sint64](Sint64)) Returns the current offset in the stream, or -1 if the
information can not be determined.

## Remarks

[SDL_TellIO](SDL_TellIO) is actually a wrapper function that calls the
[SDL_IOStream](SDL_IOStream)'s `seek` method, with an offset of 0 bytes
from [`SDL_IO_SEEK_CUR`](SDL_IO_SEEK_CUR), to simplify application
development.

## Thread Safety

Do not use the same [SDL_IOStream](SDL_IOStream) from two threads at once.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SeekIO](SDL_SeekIO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

