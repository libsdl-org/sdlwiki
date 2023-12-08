###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_WriteBE16

Use this function to write 16 bits in native format to a [SDL_RWops](SDL_RWops.md) as big-endian data.

## Syntax

```c
size_t SDL_WriteBE16(SDL_RWops * dst, Uint16 value);

```

## Function Parameters

|               |                                          |
| ------------- | ---------------------------------------- |
| **dst**       | the stream to which data will be written |
| **value**     | the data to be written, in native format |

## Return Value

Returns 1 on successful write, 0 on error.

## Remarks

SDL byteswaps the data only if necessary, so the application always
specifies native format, and the data written will be in big-endian format.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_WriteLE16](SDL_WriteLE16.md)

----
[CategoryAPI](CategoryAPI.md)
