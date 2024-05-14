###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_IOFromMem

Use this function to prepare a read-write memory buffer for use with [SDL_IOStream](SDL_IOStream).

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
SDL_IOStream* SDL_IOFromMem(void *mem, size_t size);

```

## Function Parameters

|              |                                                                      |
| ------------ | -------------------------------------------------------------------- |
| **mem**      | a pointer to a buffer to feed an [SDL_IOStream](SDL_IOStream) stream |
| **size**     | the buffer size, in bytes                                            |

## Return Value

Returns a pointer to a new [SDL_IOStream](SDL_IOStream) structure, or NULL
if it fails; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function sets up an [SDL_IOStream](SDL_IOStream) struct based on a
memory area of a certain size, for both read and write access.

This memory buffer is not copied by the [SDL_IOStream](SDL_IOStream); the
pointer you provide must remain valid until you close the stream. Closing
the stream will not free the original buffer.

If you need to make sure the [SDL_IOStream](SDL_IOStream) never writes to
the memory buffer, you should use
[SDL_IOFromConstMem](SDL_IOFromConstMem)() with a read-only buffer of
memory instead.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_IOFromConstMem](SDL_IOFromConstMem)
- [SDL_CloseIO](SDL_CloseIO)
- [SDL_ReadIO](SDL_ReadIO)
- [SDL_SeekIO](SDL_SeekIO)
- [SDL_TellIO](SDL_TellIO)
- [SDL_WriteIO](SDL_WriteIO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

