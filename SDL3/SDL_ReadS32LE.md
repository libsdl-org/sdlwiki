# SDL_ReadS32LE

Use this function to read 32 bits of little-endian data from an [SDL_IOStream](SDL_IOStream) and return in native format.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
bool SDL_ReadS32LE(SDL_IOStream *src, Sint32 *value);
```

## Function Parameters

|                                |           |                                         |
| ------------------------------ | --------- | --------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **src**   | the stream from which to read data.     |
| [Sint32](Sint32) *             | **value** | a pointer filled in with the data read. |

## Return Value

(bool) Returns true on successful read or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

SDL byteswaps the data only if necessary, so the data returned will be in
the native byte order.

This function will return false when the data stream is completely read,
and [SDL_GetIOStatus](SDL_GetIOStatus)() will return
[SDL_IO_STATUS_EOF](SDL_IO_STATUS_EOF). If false is returned and the stream
is not at EOF, [SDL_GetIOStatus](SDL_GetIOStatus)() will return a different
error value and [SDL_GetError](SDL_GetError)() will offer a human-readable
message.

## Thread Safety

Do not use the same [SDL_IOStream](SDL_IOStream) from two threads at once.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

