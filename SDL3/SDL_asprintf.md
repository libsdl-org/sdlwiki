###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_asprintf

This works exactly like asprintf() but doesn't require access to a C runtime.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_asprintf(char **strp, const char *fmt, ...);
```

## Function Parameters

|              |          |                                                        |
| ------------ | -------- | ------------------------------------------------------ |
| char **      | **strp** | on output, is set to the new string. Must not be NULL. |
| const char * | **fmt**  | a printf-style format string. Must not be NULL.        |
| ...          | **...**  | a list of values to be used with the format string.    |

## Return Value

(int) Returns the number of bytes in the newly-allocated string, not
counting the null-terminator char, or a negative value on error.

## Remarks

Functions identically to [SDL_snprintf](SDL_snprintf)(), except it
allocates a buffer large enough to hold the output string on behalf of the
caller.

On success, this function returns the number of bytes (not characters)
comprising the output string, not counting the null-terminator character,
and sets `*strp` to the newly-allocated string.

On error, this function returns a negative number, and the value of `*strp`
is undefined.

The returned string is owned by the caller, and should be passed to
[SDL_free](SDL_free) when no longer needed.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

