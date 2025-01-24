# SDL_WriteU64BE

Use this function to write 64 bits in native format to an [SDL_IOStream](SDL_IOStream) as big-endian data.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
bool SDL_WriteU64BE(SDL_IOStream *dst, Uint64 value);
```

## Function Parameters

|                                |           |                                           |
| ------------------------------ | --------- | ----------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **dst**   | the stream to which data will be written. |
| [Uint64](Uint64)               | **value** | the data to be written, in native format. |

## Return Value

(bool) Returns true on successful write or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

SDL byteswaps the data only if necessary, so the application always
specifies native format, and the data written will be in big-endian format.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

