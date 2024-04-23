###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_IOStreamInterface

The function pointers that drive an [SDL_IOStream](SDL_IOStream).

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
typedef struct SDL_IOStreamInterface
{
    /**
     *  Return the number of bytes in this SDL_IOStream
     *
     *  \return the total size of the data stream, or -1 on error.
     */
    Sint64 (SDLCALL *size)(void *userdata);

    /**
     *  Seek to \c offset relative to \c whence, one of stdio's whence values:
     *  SDL_IO_SEEK_SET, SDL_IO_SEEK_CUR, SDL_IO_SEEK_END
     *
     *  \return the final offset in the data stream, or -1 on error.
     */
    Sint64 (SDLCALL *seek)(void *userdata, Sint64 offset, int whence);

    /**
     *  Read up to \c size bytes from the data stream to the area pointed
     *  at by \c ptr.
     *
     *  On an incomplete read, you should set `*status` to a value from the
     *  SDL_IOStatus enum. You do not have to explicitly set this on
     *  a complete, successful read.
     *
     *  \return the number of bytes read
     */
    size_t (SDLCALL *read)(void *userdata, void *ptr, size_t size, SDL_IOStatus *status);

    /**
     *  Write exactly \c size bytes from the area pointed at by \c ptr
     *  to data stream.
     *
     *  On an incomplete write, you should set `*status` to a value from the
     *  SDL_IOStatus enum. You do not have to explicitly set this on
     *  a complete, successful write.
     *
     *  \return the number of bytes written
     */
    size_t (SDLCALL *write)(void *userdata, const void *ptr, size_t size, SDL_IOStatus *status);

    /**
     *  Close and free any allocated resources.
     *
     *  The SDL_IOStream is still destroyed even if this fails, so clean up anything
     *  even if flushing to disk returns an error.
     *
     *  \return 0 if successful or -1 on write error when flushing data.
     */
    int (SDLCALL *close)(void *userdata);
} SDL_IOStreamInterface;
```

## Remarks

Applications can provide this struct to [SDL_OpenIO](SDL_OpenIO)() to
create their own implementation of [SDL_IOStream](SDL_IOStream). This is
not necessarily required, as SDL already offers several common types of I/O
streams, via functions like [SDL_IOFromFile](SDL_IOFromFile)() and
[SDL_IOFromMem](SDL_IOFromMem)().

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

