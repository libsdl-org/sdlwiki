###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RWtell

Determine the current read/write offset in an [SDL_RWops](SDL_RWops.md) data stream.

## Syntax

```c
Sint64 SDL_RWtell(SDL_RWops *context);

```

## Function Parameters

|                 |                                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| **context**     | a [SDL_RWops](SDL_RWops.md) data stream object from which to get the current offset |

## Return Value

Returns the current offset in the stream, or -1 if the information can not
be determined.

## Remarks

[SDL_RWtell](SDL_RWtell.md) is actually a wrapper function that calls the
[SDL_RWops](SDL_RWops.md)'s `seek` method, with an offset of 0 bytes from
`RW_SEEK_CUR`, to simplify application development.

Prior to SDL 2.0.10, this function was a macro.

## Version

This function is available since SDL 2.0.10.

## Related Functions

* [SDL_RWclose](SDL_RWclose.md)
* [SDL_RWFromConstMem](SDL_RWFromConstMem.md)
* [SDL_RWFromFile](SDL_RWFromFile.md)
* [SDL_RWFromFP](SDL_RWFromFP.md)
* [SDL_RWFromMem](SDL_RWFromMem.md)
* [SDL_RWread](SDL_RWread.md)
* [SDL_RWseek](SDL_RWseek.md)
* [SDL_RWwrite](SDL_RWwrite.md)

----
[CategoryAPI](CategoryAPI.md)
