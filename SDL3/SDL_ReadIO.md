###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReadIO

Read from a data source.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
size_t SDL_ReadIO(SDL_IOStream *context, void *ptr, size_t size);
```

## Function Parameters

|                                |             |                                                        |
| ------------------------------ | ----------- | ------------------------------------------------------ |
| [SDL_IOStream](SDL_IOStream) * | **context** | a pointer to an [SDL_IOStream](SDL_IOStream) structure |
| void *                         | **ptr**     | a pointer to a buffer to read data into                |
| size_t                         | **size**    | the number of bytes to read from the data source.      |

## Return Value

(size_t) Returns the number of bytes read, or 0 on end of file or other
error.

## Remarks

This function reads up `size` bytes from the data source to the area
pointed at by `ptr`. This function may read less bytes than requested. It
will return zero when the data stream is completely read, or on error. To
determine if there was an error or all data was read, call
[SDL_GetIOStatus](SDL_GetIOStatus)().

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_WriteIO](SDL_WriteIO)
- [SDL_GetIOStatus](SDL_GetIOStatus)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

