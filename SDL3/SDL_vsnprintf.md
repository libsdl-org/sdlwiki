###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_vsnprintf

This works exactly like vsnprintf() but doesn't require access to a C runtime.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_vsnprintf(char *text, size_t maxlen, const char *fmt, va_list ap);
```

## Function Parameters

|              |            |                                                            |
| ------------ | ---------- | ---------------------------------------------------------- |
| char *       | **text**   | the buffer to write the string into. Must not be NULL.     |
| size_t       | **maxlen** | the maximum bytes to write, including the null-terminator. |
| const char * | **fmt**    | a printf-style format string. Must not be NULL.            |
| va_list      | **ap**     | a `va_list` values to be used with the format string.      |

## Return Value

(int) Returns the number of bytes that should be written, not counting the
null-terminator char, or a negative value on error.

## Remarks

Functions identically to [SDL_snprintf](SDL_snprintf)(), except it takes a
`va_list` instead of using `...` variable arguments.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

