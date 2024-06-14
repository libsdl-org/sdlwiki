###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReadS64LE

Use this function to read 64 bits of little-endian data from an [SDL_IOStream](SDL_IOStream) and return in native format.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
SDL_bool SDL_ReadS64LE(SDL_IOStream *src, Sint64 *value);
```

## Function Parameters

|                                |           |                                         |
| ------------------------------ | --------- | --------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **src**   | the stream from which to read data.     |
| Sint64 *                       | **value** | a pointer filled in with the data read. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on successful write,
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

SDL byteswaps the data only if necessary, so the data returned will be in
the native byte order.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

