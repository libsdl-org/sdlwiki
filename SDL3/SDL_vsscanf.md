###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_vsscanf

This works exactly like vsscanf() but doesn't require access to a C runtime.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_vsscanf(const char *text, const char *fmt, va_list ap);
```

## Function Parameters

|              |          |                                                                       |
| ------------ | -------- | --------------------------------------------------------------------- |
| const char * | **text** | the string to scan. Must not be NULL.                                 |
| const char * | **fmt**  | a printf-style format string. Must not be NULL.                       |
| va_list      | **ap**   | a `va_list` of pointers to values to be filled in with scanned items. |

## Return Value

(int) Returns the number of items that matched the format string.

## Remarks

Functions identically to [SDL_sscanf](SDL_sscanf)(), except it takes a
`va_list` instead of using `...` variable arguments.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

