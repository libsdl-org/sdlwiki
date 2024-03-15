###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReadIO

Read from a data source.

## Syntax

```c
size_t SDL_ReadIO(SDL_IOStream *context, void *ptr, size_t size);

```

## Function Parameters

|                 |                                                        |
| --------------- | ------------------------------------------------------ |
| **context**     | a pointer to an [SDL_IOStream](SDL_IOStream) structure |
| **ptr**         | a pointer to a buffer to read data into                |
| **size**        | the number of bytes to read from the data source.      |

## Return Value

Returns the number of bytes read, or 0 on end of file or other error.

## Remarks

This function reads up `size` bytes from the data source to the area
pointed at by `ptr`. This function may read less bytes than requested. It
will return zero when the data stream is completely read, or -1 on error.
For streams that support non-blocking operation, if nothing was read
because it would require blocking, this function returns -2 to distinguish
that this is not an error or end-of-file, and the caller can try again
later.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_IOFromConstMem](SDL_IOFromConstMem)
* [SDL_IOFromFile](SDL_IOFromFile)
* [SDL_IOFromMem](SDL_IOFromMem)
* [SDL_SeekIO](SDL_SeekIO)
* [SDL_WriteIO](SDL_WriteIO)

----
[CategoryAPI](CategoryAPI)

