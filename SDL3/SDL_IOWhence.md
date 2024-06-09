###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_IOWhence

Possible `whence` values for [SDL_IOStream](SDL_IOStream) seeking.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
typedef enum SDL_IOWhence
{
    SDL_IO_SEEK_SET,  /**< Seek from the beginning of data */
    SDL_IO_SEEK_CUR,  /**< Seek relative to current read point */
    SDL_IO_SEEK_END,  /**< Seek relative to the end of data */
} SDL_IOWhence;
```

## Remarks

These map to the same "whence" concept that `fseek` or `lseek` use in the
standard C runtime.

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryIOStream](CategoryIOStream)

