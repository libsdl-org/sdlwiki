# SDL_ReadIO

Read from a data source.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
size_t SDL_ReadIO(SDL_IOStream *context, void *ptr, size_t size);
```

## Function Parameters

|                                |             |                                                         |
| ------------------------------ | ----------- | ------------------------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **context** | a pointer to an [SDL_IOStream](SDL_IOStream) structure. |
| void *                         | **ptr**     | a pointer to a buffer to read data into.                |
| size_t                         | **size**    | the number of bytes to read from the data source.       |

## Return Value

(size_t) Returns the number of bytes read, or 0 on end of file or other
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function reads up `size` bytes from the data source to the area
pointed at by `ptr`. This function may read less bytes than requested.

This function will return zero when the data stream is completely read, and
[SDL_GetIOStatus](SDL_GetIOStatus)() will return
[SDL_IO_STATUS_EOF](SDL_IO_STATUS_EOF). If zero is returned and the stream
is not at EOF, [SDL_GetIOStatus](SDL_GetIOStatus)() will return a different
error value and [SDL_GetError](SDL_GetError)() will offer a human-readable
message.

## Thread Safety

Do not use the same [SDL_IOStream](SDL_IOStream) from two threads at once.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_WriteIO](SDL_WriteIO)
- [SDL_GetIOStatus](SDL_GetIOStatus)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

