###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WriteLE16

Use this function to write 16 bits in native format to a [SDL_RWops](SDL_RWops.md) as little-endian data.

## Syntax

```c
size_t SDL_WriteLE16(SDL_RWops * dst, Uint16 value);

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
specifies native format, and the data written will be in little-endian
format.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_WriteBE16](SDL_WriteBE16.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryIO](CategoryIO.md)
