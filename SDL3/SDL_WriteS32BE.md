###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WriteS32BE

Use this function to write 32 bits in native format to an [SDL_IOStream](SDL_IOStream) as big-endian data.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
SDL_bool SDL_WriteS32BE(SDL_IOStream *dst, Sint32 value);
```

## Function Parameters

|                                |           |                                           |
| ------------------------------ | --------- | ----------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **dst**   | the stream to which data will be written. |
| Sint32                         | **value** | the data to be written, in native format. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on successful write,
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

SDL byteswaps the data only if necessary, so the application always
specifies native format, and the data written will be in big-endian format.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

