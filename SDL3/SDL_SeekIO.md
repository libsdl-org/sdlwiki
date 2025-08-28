# SDL_SeekIO

Seek within an [SDL_IOStream](SDL_IOStream) data stream.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
Sint64 SDL_SeekIO(SDL_IOStream *context, Sint64 offset, SDL_IOWhence whence);
```

## Function Parameters

|                                |             |                                                                                                                          |
| ------------------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------ |
| [SDL_IOStream](SDL_IOStream) * | **context** | a pointer to an [SDL_IOStream](SDL_IOStream) structure.                                                                  |
| [Sint64](Sint64)               | **offset**  | an offset in bytes, relative to `whence` location; can be negative.                                                      |
| [SDL_IOWhence](SDL_IOWhence)   | **whence**  | any of [`SDL_IO_SEEK_SET`](SDL_IO_SEEK_SET), [`SDL_IO_SEEK_CUR`](SDL_IO_SEEK_CUR), [`SDL_IO_SEEK_END`](SDL_IO_SEEK_END). |

## Return Value

([Sint64](Sint64)) Returns the final offset in the data stream after the
seek or -1 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

This function seeks to byte `offset`, relative to `whence`.

`whence` may be any of the following values:

- [`SDL_IO_SEEK_SET`](SDL_IO_SEEK_SET): seek from the beginning of data
- [`SDL_IO_SEEK_CUR`](SDL_IO_SEEK_CUR): seek relative to current read point
- [`SDL_IO_SEEK_END`](SDL_IO_SEEK_END): seek relative to the end of data

If this stream can not seek, it will return -1.

## Thread Safety

Do not use the same [SDL_IOStream](SDL_IOStream) from two threads at once.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_TellIO](SDL_TellIO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

