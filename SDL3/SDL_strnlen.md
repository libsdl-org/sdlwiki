# SDL_strnlen

This works exactly like strnlen() but doesn't require access to a C runtime.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
size_t SDL_strnlen(const char *str, size_t maxlen);
```

## Function Parameters

|              |            |                                                       |
| ------------ | ---------- | ----------------------------------------------------- |
| const char * | **str**    | The null-terminated string to read. Must not be NULL. |
| size_t       | **maxlen** | The maximum amount of bytes to count.                 |

## Return Value

(size_t) Returns the length (in bytes, excluding the null terminator) of
`src` but never more than `maxlen`.

## Remarks

Counts up to a maximum of `maxlen` bytes in `str`, excluding the null
terminator.

If you need the length of a UTF-8 string, consider using
[SDL_utf8strnlen](SDL_utf8strnlen)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_strlen](SDL_strlen)
- [SDL_utf8strlen](SDL_utf8strlen)
- [SDL_utf8strnlen](SDL_utf8strnlen)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

