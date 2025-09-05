# SDL_IOStreamInterface

The function pointers that drive an [SDL_IOStream](SDL_IOStream).

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
typedef struct SDL_IOStreamInterface
{
    /* The version of this interface */
    Uint32 version;

    /**
     *  Return the number of bytes in this SDL_IOStream
     *
     *  \return the total size of the data stream, or -1 on error.
     */
    Sint64 (SDLCALL *size)(void *userdata);

    /**
     *  Seek to `offset` relative to `whence`, one of stdio's whence values:
     *  SDL_IO_SEEK_SET, SDL_IO_SEEK_CUR, SDL_IO_SEEK_END
     *
     *  \return the final offset in the data stream, or -1 on error.
     */
    Sint64 (SDLCALL *seek)(void *userdata, Sint64 offset, SDL_IOWhence whence);

    /**
     *  Read up to `size` bytes from the data stream to the area pointed
     *  at by `ptr`. `size` will always be > 0.
     *
     *  On an incomplete read, you should set `*status` to a value from the
     *  SDL_IOStatus enum. You do not have to explicitly set this on
     *  a complete, successful read.
     *
     *  \return the number of bytes read
     */
    size_t (SDLCALL *read)(void *userdata, void *ptr, size_t size, SDL_IOStatus *status);

    /**
     *  Write exactly `size` bytes from the area pointed at by `ptr`
     *  to data stream. `size` will always be > 0.
     *
     *  On an incomplete write, you should set `*status` to a value from the
     *  SDL_IOStatus enum. You do not have to explicitly set this on
     *  a complete, successful write.
     *
     *  \return the number of bytes written
     */
    size_t (SDLCALL *write)(void *userdata, const void *ptr, size_t size, SDL_IOStatus *status);

    /**
     *  If the stream is buffering, make sure the data is written out.
     *
     *  On failure, you should set `*status` to a value from the
     *  SDL_IOStatus enum. You do not have to explicitly set this on
     *  a successful flush.
     *
     *  \return true if successful or false on write error when flushing data.
     */
    bool (SDLCALL *flush)(void *userdata, SDL_IOStatus *status);

    /**
     *  Close and free any allocated resources.
     *
     *  This does not guarantee file writes will sync to physical media; they
     *  can be in the system's file cache, waiting to go to disk.
     *
     *  The SDL_IOStream is still destroyed even if this fails, so clean up anything
     *  even if flushing buffers, etc, returns an error.
     *
     *  \return true if successful or false on write error when flushing data.
     */
    bool (SDLCALL *close)(void *userdata);

} SDL_IOStreamInterface;
```

## Remarks

Applications can provide this struct to [SDL_OpenIO](SDL_OpenIO)() to
create their own implementation of [SDL_IOStream](SDL_IOStream). This is
not necessarily required, as SDL already offers several common types of I/O
streams, via functions like [SDL_IOFromFile](SDL_IOFromFile)() and
[SDL_IOFromMem](SDL_IOFromMem)().

This structure should be initialized using
[SDL_INIT_INTERFACE](SDL_INIT_INTERFACE)()

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_INIT_INTERFACE](SDL_INIT_INTERFACE)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryIOStream](CategoryIOStream)

