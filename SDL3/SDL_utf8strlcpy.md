# SDL_utf8strlcpy

Copy an UTF-8 string.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
size_t SDL_utf8strlcpy(char *dst, const char *src, size_t dst_bytes);
```

## Function Parameters

|              |               |                                                                                              |
| ------------ | ------------- | -------------------------------------------------------------------------------------------- |
| char *       | **dst**       | The destination buffer. Must not be NULL, and must not overlap with `src`.                   |
| const char * | **src**       | The null-terminated UTF-8 string to copy. Must not be NULL, and must not overlap with `dst`. |
| size_t       | **dst_bytes** | The length (in bytes) of the destination buffer. Must not be 0.                              |

## Return Value

(size_t) Returns the number of bytes written, excluding the null
terminator.

## Remarks

This function copies up to `dst_bytes` - 1 bytes from `src` to `dst` while
also ensuring that the string written to `dst` does not end in a truncated
multi-byte sequence. Finally, it appends a null terminator.

`src` and `dst` must not overlap.

Note that unlike [SDL_strlcpy](SDL_strlcpy)(), this function returns the
number of bytes written, not the length of `src`.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_strlcpy](SDL_strlcpy)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

