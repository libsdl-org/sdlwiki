###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ReadBE64

Use this function to read 64 bits of big-endian data from an [SDL_RWops](SDL_RWops) and return in native format.

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
Uint64 SDL_ReadBE64(SDL_RWops * src);

```

## Function Parameters

|             |                                    |
| ----------- | ---------------------------------- |
| **src**     | the stream from which to read data |

## Return Value

Returns 64 bits of data in the native byte order of the platform.

## Remarks

SDL byteswaps the data only if necessary, so the data returned will be in
the native byte order.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_ReadLE64](SDL_ReadLE64)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

