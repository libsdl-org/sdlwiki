###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RWseek

Seek within an [SDL_RWops](SDL_RWops.md) data stream.

## Syntax

```c
Sint64 SDL_RWseek(SDL_RWops *context, Sint64 offset, int whence);

```

## Function Parameters

|                 |                                                                                                                         |
| --------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **context**     | a pointer to an [SDL_RWops](SDL_RWops.md) structure                                                                        |
| **offset**      | an offset in bytes, relative to **whence** location; can be negative                                                    |
| **whence**      | any of [`SDL_RW_SEEK_SET`](SDL_RW_SEEK_SET), [`SDL_RW_SEEK_CUR`](SDL_RW_SEEK_CUR), [`SDL_RW_SEEK_END`](SDL_RW_SEEK_END) |

## Return Value

Returns the final offset in the data stream after the seek or a negative
error code on failure; call [SDL_GetError](SDL_GetError.md)() for more
information.

## Remarks

This function seeks to byte `offset`, relative to `whence`.

`whence` may be any of the following values:

- [`SDL_RW_SEEK_SET`](SDL_RW_SEEK_SET): seek from the beginning of data
- [`SDL_RW_SEEK_CUR`](SDL_RW_SEEK_CUR): seek relative to current read point
- [`SDL_RW_SEEK_END`](SDL_RW_SEEK_END): seek relative to the end of data

If this stream can not seek, it will return -1.

[SDL_RWseek](SDL_RWseek.md)() is actually a wrapper function that calls the
[SDL_RWops](SDL_RWops.md)'s `seek` method appropriately, to simplify
application development.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
SDL_RWops *rw = SDL_RWFromFile("myfile.bin", "rb");
if (rw != NULL) {
    /* Seek to 0 bytes from the end of the file */
    Sint64 length = SDL_RWseek(rw, 0, SDL_RW_SEEK_END);
    SDL_RWclose(rw);
    if (length < 0) {
        printf("Could not seek inside myfile.bin\n");
    } else {
        printf("myfile.bin is %d bytes long\n", length);
    }
}
```

## Related Functions

* [SDL_RWclose](SDL_RWclose.md)
* [SDL_RWFromConstMem](SDL_RWFromConstMem.md)
* [SDL_RWFromFile](SDL_RWFromFile.md)
* [SDL_RWFromMem](SDL_RWFromMem.md)
* [SDL_RWread](SDL_RWread.md)
* [SDL_RWtell](SDL_RWtell.md)
* [SDL_RWwrite](SDL_RWwrite.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryIO](CategoryIO.md)
