# SDL_WriteU64LE

Use this function to write 64 bits in native format to an [SDL_IOStream](SDL_IOStream) as little-endian data.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
bool SDL_WriteU64LE(SDL_IOStream *dst, Uint64 value);
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
specifies native format, and the data written will be in little-endian
format.

## Thread Safety

Do not use the same [SDL_IOStream](SDL_IOStream) from two threads at once.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

