# SDL_sscanf

This works exactly like sscanf() but doesn't require access to a C runtime.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_sscanf(const char *text, const char *fmt, ...);
```

## Function Parameters

|              |          |                                                                  |
| ------------ | -------- | ---------------------------------------------------------------- |
| const char * | **text** | the string to scan. Must not be NULL.                            |
| const char * | **fmt**  | a printf-style format string. Must not be NULL.                  |
| ...          | **...**  | a list of pointers to values to be filled in with scanned items. |

## Return Value

(int) Returns the number of items that matched the format string.

## Remarks

Scan a string, matching a format string, converting each '%' item and
storing it to pointers provided through variable arguments.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

