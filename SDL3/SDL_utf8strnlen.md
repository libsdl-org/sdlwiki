###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_utf8strnlen

Count the number of codepoints in a UTF-8 string, up to n bytes.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
size_t SDL_utf8strnlen(const char *str, size_t bytes);
```

## Function Parameters

|              |           |                                                             |
| ------------ | --------- | ----------------------------------------------------------- |
| const char * | **str**   | The null-terminated UTF-8 string to read. Must not be NULL. |
| size_t       | **bytes** | The maximum amount of bytes to count.                       |

## Return Value

(size_t) Returns The length (in codepoints, excluding the null terminator)
of `src` but never more than `maxlen`.

## Remarks

Counts the _codepoints_, not _bytes_, in `str`, excluding the null
terminator.

If you need to count the bytes in a string instead, consider using
[SDL_strnlen](SDL_strnlen)().

The counting stops at `bytes` bytes (not codepoints!). This seems
counterintuitive, but makes it easy to express the total size of the
string's buffer.

Since this handles Unicode, it expects the strings to be well-formed UTF-8
and not a null-terminated string of arbitrary bytes. Bytes that are not
valid UTF-8 are treated as Unicode character U+FFFD (REPLACEMENT
CHARACTER), so a malformed or incomplete UTF-8 sequence might increase the
count by several replacement characters.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_utf8strlen](SDL_utf8strlen)
- [SDL_strnlen](SDL_strnlen)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

