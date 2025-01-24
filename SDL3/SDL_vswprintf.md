# SDL_vswprintf

This works exactly like vswprintf() but doesn't require access to a C runtime.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_vswprintf(wchar_t *text, size_t maxlen, const wchar_t *fmt, va_list ap);
```

## Function Parameters

|                 |            |                                                                      |
| --------------- | ---------- | -------------------------------------------------------------------- |
| wchar_t *       | **text**   | the buffer to write the string into. Must not be NULL.               |
| size_t          | **maxlen** | the maximum wide characters to write, including the null-terminator. |
| const wchar_t * | **fmt**    | a printf-style format wide string. Must not be NULL.                 |
| va_list         | **ap**     | a `va_list` values to be used with the format string.                |

## Return Value

(int) Returns the number of wide characters that should be written, not
counting the null-terminator char, or a negative value on error.

## Remarks

Functions identically to [SDL_swprintf](SDL_swprintf)(), except it takes a
`va_list` instead of using `...` variable arguments.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

