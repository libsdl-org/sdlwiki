###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_IOStatus

[SDL_IOStream](SDL_IOStream) status, set by a read or write operation.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
typedef enum SDL_IOStatus
{
    SDL_IO_STATUS_READY,     /**< Everything is ready (no errors and not EOF). */
    SDL_IO_STATUS_ERROR,     /**< Read or write I/O error */
    SDL_IO_STATUS_EOF,       /**< End of file */
    SDL_IO_STATUS_NOT_READY, /**< Non blocking I/O, not ready */
    SDL_IO_STATUS_READONLY,  /**< Tried to write a read-only buffer */
    SDL_IO_STATUS_WRITEONLY  /**< Tried to read a write-only buffer */
} SDL_IOStatus;
```

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryIOStream](CategoryIOStream)

