###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SeekIO

Seek within an [SDL_IOStream](SDL_IOStream) data stream.

## Syntax

```c
Sint64 SDL_SeekIO(SDL_IOStream *context, Sint64 offset, int whence);

```

## Function Parameters

|                 |                                                                                                                         |
| --------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **context**     | a pointer to an [SDL_IOStream](SDL_IOStream) structure                                                                  |
| **offset**      | an offset in bytes, relative to **whence** location; can be negative                                                    |
| **whence**      | any of [`SDL_IO_SEEK_SET`](SDL_IO_SEEK_SET), [`SDL_IO_SEEK_CUR`](SDL_IO_SEEK_CUR), [`SDL_IO_SEEK_END`](SDL_IO_SEEK_END) |

## Return Value

Returns the final offset in the data stream after the seek or a negative
error code on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

This function seeks to byte `offset`, relative to `whence`.

`whence` may be any of the following values:

- [`SDL_IO_SEEK_SET`](SDL_IO_SEEK_SET): seek from the beginning of data
- [`SDL_IO_SEEK_CUR`](SDL_IO_SEEK_CUR): seek relative to current read point
- [`SDL_IO_SEEK_END`](SDL_IO_SEEK_END): seek relative to the end of data

If this stream can not seek, it will return -1.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_IOFromConstMem](SDL_IOFromConstMem)
* [SDL_IOFromFile](SDL_IOFromFile)
* [SDL_IOFromMem](SDL_IOFromMem)
* [SDL_ReadIO](SDL_ReadIO)
* [SDL_TellIO](SDL_TellIO)
* [SDL_WriteIO](SDL_WriteIO)

----
[CategoryAPI](CategoryAPI)

