###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_WriteS64BE

Use this function to write 64 bits in native format to an [SDL_IOStream](SDL_IOStream) as big-endian data.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
bool SDL_WriteS64BE(SDL_IOStream *dst, Sint64 value);
```

## Function Parameters

|                                |           |                                           |
| ------------------------------ | --------- | ----------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **dst**   | the stream to which data will be written. |
| Sint64                         | **value** | the data to be written, in native format. |

## Return Value

(bool) Returns true on successful write or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

SDL byteswaps the data only if necessary, so the application always
specifies native format, and the data written will be in big-endian format.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

