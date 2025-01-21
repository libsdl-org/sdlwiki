###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_IOprintf

Print to an [SDL_IOStream](SDL_IOStream) data stream.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
size_t SDL_IOprintf(SDL_IOStream *context, const char *fmt, ...);
```

## Function Parameters

|                                |             |                                                                      |
| ------------------------------ | ----------- | -------------------------------------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **context** | a pointer to an [SDL_IOStream](SDL_IOStream) structure.              |
| const char *                   | **fmt**     | a printf() style format string.                                      |
| ...                            | **...**     | additional parameters matching % tokens in the `fmt` string, if any. |

## Return Value

(size_t) Returns the number of bytes written or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function does formatted printing to the stream.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_IOvprintf](SDL_IOvprintf)
- [SDL_WriteIO](SDL_WriteIO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

