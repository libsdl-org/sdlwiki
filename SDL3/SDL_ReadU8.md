# SDL_ReadU8

Use this function to read a byte from an [SDL_IOStream](SDL_IOStream).

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
bool SDL_ReadU8(SDL_IOStream *src, Uint8 *value);
```

## Function Parameters

|                                |           |                                                |
| ------------------------------ | --------- | ---------------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **src**   | the [SDL_IOStream](SDL_IOStream) to read from. |
| Uint8 *                        | **value** | a pointer filled in with the data read.        |

## Return Value

(bool) Returns true on success or false on failure or EOF; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function will return false when the data stream is completely read,
and [SDL_GetIOStatus](SDL_GetIOStatus)() will return
[SDL_IO_STATUS_EOF](SDL_IO_STATUS_EOF). If false is returned and the stream
is not at EOF, [SDL_GetIOStatus](SDL_GetIOStatus)() will return a different
error value and [SDL_GetError](SDL_GetError)() will offer a human-readable
message.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

