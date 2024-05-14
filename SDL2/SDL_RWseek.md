###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RWseek

Seek within an [SDL_RWops](SDL_RWops) data stream.

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h)

## Syntax

```c
Sint64 SDL_RWseek(SDL_RWops *context,
                  Sint64 offset, int whence);

```

## Function Parameters

|                 |                                                                      |
| --------------- | -------------------------------------------------------------------- |
| **context**     | a pointer to an [SDL_RWops](SDL_RWops) structure                     |
| **offset**      | an offset in bytes, relative to **whence** location; can be negative |
| **whence**      | any of `RW_SEEK_SET`, `RW_SEEK_CUR`, `RW_SEEK_END`                   |

## Return Value

Returns the final offset in the data stream after the seek or -1 on error.

## Remarks

This function seeks to byte `offset`, relative to `whence`.

`whence` may be any of the following values:

- `RW_SEEK_SET`: seek from the beginning of data
- `RW_SEEK_CUR`: seek relative to current read point
- `RW_SEEK_END`: seek relative to the end of data

If this stream can not seek, it will return -1.

[SDL_RWseek](SDL_RWseek)() is actually a wrapper function that calls the
[SDL_RWops](SDL_RWops)'s `seek` method appropriately, to simplify
application development.

Prior to SDL 2.0.10, this function was a macro.

## Version

This function is available since SDL 2.0.10.

## See Also

- [SDL_RWclose](SDL_RWclose)
- [SDL_RWFromConstMem](SDL_RWFromConstMem)
- [SDL_RWFromFile](SDL_RWFromFile)
- [SDL_RWFromFP](SDL_RWFromFP)
- [SDL_RWFromMem](SDL_RWFromMem)
- [SDL_RWread](SDL_RWread)
- [SDL_RWtell](SDL_RWtell)
- [SDL_RWwrite](SDL_RWwrite)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRWOPS](CategoryRWOPS)

