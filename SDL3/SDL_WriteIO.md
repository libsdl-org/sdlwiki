# SDL_WriteIO

Write to an [SDL_IOStream](SDL_IOStream) data stream.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
size_t SDL_WriteIO(SDL_IOStream *context, const void *ptr, size_t size);
```

## Function Parameters

|                                |             |                                                         |
| ------------------------------ | ----------- | ------------------------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **context** | a pointer to an [SDL_IOStream](SDL_IOStream) structure. |
| const void *                   | **ptr**     | a pointer to a buffer containing data to write.         |
| size_t                         | **size**    | the number of bytes to write.                           |

## Return Value

(size_t) Returns the number of bytes written, which will be less than
`size` on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

This function writes exactly `size` bytes from the area pointed at by `ptr`
to the stream. If this fails for any reason, it'll return less than `size`
to demonstrate how far the write progressed. On success, it returns `size`.

On error, this function still attempts to write as much as possible, so it
might return a positive value less than the requested write size.

The caller can use [SDL_GetIOStatus](SDL_GetIOStatus)() to determine if the
problem is recoverable, such as a non-blocking write that can simply be
retried later, or a fatal error.

## Thread Safety

Do not use the same [SDL_IOStream](SDL_IOStream) from two threads at once.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_IOprintf](SDL_IOprintf)
- [SDL_ReadIO](SDL_ReadIO)
- [SDL_SeekIO](SDL_SeekIO)
- [SDL_FlushIO](SDL_FlushIO)
- [SDL_GetIOStatus](SDL_GetIOStatus)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

