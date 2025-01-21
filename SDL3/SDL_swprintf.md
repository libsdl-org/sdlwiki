###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_swprintf

This works exactly like swprintf() but doesn't require access to a C runtime.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_swprintf(wchar_t *text, size_t maxlen, const wchar_t *fmt, ...);
```

## Function Parameters

|                 |            |                                                                     |
| --------------- | ---------- | ------------------------------------------------------------------- |
| wchar_t *       | **text**   | the buffer to write the wide string into. Must not be NULL.         |
| size_t          | **maxlen** | the maximum wchar_t values to write, including the null-terminator. |
| const wchar_t * | **fmt**    | a printf-style format string. Must not be NULL.                     |
| ...             | **...**    | a list of values to be used with the format string.                 |

## Return Value

(int) Returns the number of wide characters that should be written, not
counting the null-terminator char, or a negative value on error.

## Remarks

Format a wide string of up to `maxlen`-1 wchar_t values, converting each
'%' item with values provided through variable arguments.

While some C runtimes differ on how to deal with too-large strings, this
function null-terminates the output, by treating the null-terminator as
part of the `maxlen` count. Note that if `maxlen` is zero, however, no wide
characters will be written at all.

This function returns the number of _wide characters_ (not _codepoints_)
that should be written, excluding the null-terminator character. If this
returns a number >= `maxlen`, it means the output string was truncated. A
negative return value means an error occurred.

Referencing the output string's pointer with a format item is undefined
behavior.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

