###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_WriteBE16

Use this function to write 16 bits in native format to a [SDL_RWops](SDL_RWops) as big-endian data.

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h)

## Syntax

```c
size_t SDL_WriteBE16(SDL_RWops * dst, Uint16 value);
```

## Function Parameters

|                          |           |                                           |
| ------------------------ | --------- | ----------------------------------------- |
| [SDL_RWops](SDL_RWops) * | **dst**   | the stream to which data will be written. |
| Uint16                   | **value** | the data to be written, in native format. |

## Return Value

(size_t) Returns 1 on successful write, 0 on error.

## Remarks

SDL byteswaps the data only if necessary, so the application always
specifies native format, and the data written will be in big-endian format.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_WriteLE16](SDL_WriteLE16)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRWOPS](CategoryRWOPS)

