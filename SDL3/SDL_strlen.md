###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_strlen

This works exactly like strlen() but doesn't require access to a C runtime.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
size_t SDL_strlen(const char *str);
```

## Function Parameters

|              |         |                                                       |
| ------------ | ------- | ----------------------------------------------------- |
| const char * | **str** | The null-terminated string to read. Must not be NULL. |

## Return Value

(size_t) Returns The length (in bytes, excluding the null terminator) of
`src`.

## Remarks

Counts the bytes in `str`, excluding the null terminator.

If you need the length of a UTF-8 string, consider using
[SDL_utf8strlen](SDL_utf8strlen)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_strnlen](SDL_strnlen)
- [SDL_utf8strlen](SDL_utf8strlen)
- [SDL_utf8strnlen](SDL_utf8strnlen)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

