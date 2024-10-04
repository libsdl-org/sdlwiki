###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_strlcpy

Copy a string.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
size_t SDL_strlcpy(char *dst, const char *src, size_t maxlen);
```

## Function Parameters

|              |            |                                                                                        |
| ------------ | ---------- | -------------------------------------------------------------------------------------- |
| char *       | **dst**    | The destination buffer. Must not be NULL, and must not overlap with `src`.             |
| const char * | **src**    | The null-terminated string to copy. Must not be NULL, and must not overlap with `dst`. |
| size_t       | **maxlen** | The length (in characters) of the destination buffer.                                  |

## Return Value

(size_t) Returns The length (in characters, excluding the null terminator)
of `src`.

## Remarks

This function copies up to `maxlen` - 1 characters from `src` to `dst`,
then appends a null terminator.

If `maxlen` is 0, no characters are copied and no null terminator is
written.

If you want to copy an UTF-8 string but need to ensure that multi-byte
sequences are not truncated, consider using
[SDL_utf8strlcpy](SDL_utf8strlcpy)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_strlcat](SDL_strlcat)
- [SDL_utf8strlcpy](SDL_utf8strlcpy)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

