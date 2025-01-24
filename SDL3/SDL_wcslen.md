# SDL_wcslen

This works exactly like wcslen() but doesn't require access to a C runtime.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
size_t SDL_wcslen(const wchar_t *wstr);
```

## Function Parameters

|                 |          |                                                            |
| --------------- | -------- | ---------------------------------------------------------- |
| const wchar_t * | **wstr** | The null-terminated wide string to read. Must not be NULL. |

## Return Value

(size_t) Returns the length (in wchar_t values, excluding the null
terminator) of `wstr`.

## Remarks

Counts the number of wchar_t values in `wstr`, excluding the null
terminator.

Like [SDL_strlen](SDL_strlen) only counts bytes and not codepoints in a
UTF-8 string, this counts wchar_t values in a string, even if the string's
encoding is of variable width, like UTF-16.

Also be aware that wchar_t is different sizes on different platforms (4
bytes on Linux, 2 on Windows, etc).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_wcsnlen](SDL_wcsnlen)
- [SDL_utf8strlen](SDL_utf8strlen)
- [SDL_utf8strnlen](SDL_utf8strnlen)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

