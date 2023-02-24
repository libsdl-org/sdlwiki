###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ReadBE32

Use this function to read 32 bits of big-endian data from an [SDL_RWops](SDL_RWops) and return in native format.

## Syntax

```c
Uint32 SDL_ReadBE32(SDL_RWops * src);

```

## Function Parameters

|             |                                    |
| ----------- | ---------------------------------- |
| **src**     | the stream from which to read data |

## Return Value

Returns 32 bits of data in the native byte order of the platform.

## Remarks

SDL byteswaps the data only if necessary, so the data returned will be in
the native byte order.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_ReadLE32](SDL_ReadLE32)

----
[CategoryAPI](CategoryAPI)

