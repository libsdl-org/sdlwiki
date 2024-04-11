###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RWtell

Determine the current read/write offset in an [SDL_RWops](SDL_RWops) data stream.

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
Sint64 SDL_RWtell(SDL_RWops *context);

```

## Function Parameters

|                 |                                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| **context**     | a [SDL_RWops](SDL_RWops) data stream object from which to get the current offset |

## Return Value

Returns the current offset in the stream, or -1 if the information can not
be determined.

## Remarks

[SDL_RWtell](SDL_RWtell) is actually a wrapper function that calls the
[SDL_RWops](SDL_RWops)'s `seek` method, with an offset of 0 bytes from
`RW_SEEK_CUR`, to simplify application development.

Prior to SDL 2.0.10, this function was a macro.

## Version

This function is available since SDL 2.0.10.

## See Also

* [SDL_RWclose](SDL_RWclose)
* [SDL_RWFromConstMem](SDL_RWFromConstMem)
* [SDL_RWFromFile](SDL_RWFromFile)
* [SDL_RWFromFP](SDL_RWFromFP)
* [SDL_RWFromMem](SDL_RWFromMem)
* [SDL_RWread](SDL_RWread)
* [SDL_RWseek](SDL_RWseek)
* [SDL_RWwrite](SDL_RWwrite)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

