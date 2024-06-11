###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_strcmp

Compare two null-terminated UTF-8 strings.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_strcmp(const char *str1, const char *str2);
```

## Function Parameters

|              |                                                      |
| ------------ | ---------------------------------------------------- |
| **str1**     | The first string to compare. NULL is not permitted!  |
| **str2**     | The second string to compare. NULL is not permitted! |

## Return Value

Returns less than zero if str1 is "less than" str2, greater than zero if
str1 is "greater than" str2, and zero if the strings match exactly.

## Remarks

Due to the nature of UTF-8 encoding, this will work with Unicode strings,
since effectively this function just compares bytes until it hits a
null-terminating character. Also due to the nature of UTF-8, this can be
used with [SDL_qsort](SDL_qsort)() to put strings in (roughly) alphabetical
order.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

