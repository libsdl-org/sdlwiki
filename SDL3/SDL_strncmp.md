# SDL_strncmp

Compare two UTF-8 strings up to a number of bytes.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_strncmp(const char *str1, const char *str2, size_t maxlen);
```

## Function Parameters

|              |            |                                                      |
| ------------ | ---------- | ---------------------------------------------------- |
| const char * | **str1**   | the first string to compare. NULL is not permitted!  |
| const char * | **str2**   | the second string to compare. NULL is not permitted! |
| size_t       | **maxlen** | the maximum number of _bytes_ to compare.            |

## Return Value

(int) Returns less than zero if str1 is "less than" str2, greater than zero
if str1 is "greater than" str2, and zero if the strings match exactly.

## Remarks

Due to the nature of UTF-8 encoding, this will work with Unicode strings,
since effectively this function just compares bytes until it hits a
null-terminating character. Also due to the nature of UTF-8, this can be
used with [SDL_qsort](SDL_qsort)() to put strings in (roughly) alphabetical
order.

Note that while this function is intended to be used with UTF-8, it is
doing a bytewise comparison, and `maxlen` specifies a _byte_ limit! If the
limit lands in the middle of a multi-byte UTF-8 sequence, it will only
compare a portion of the final character.

`maxlen` specifies a maximum number of bytes to compare; if the strings
match to this number of bytes (or both have matched to a null-terminator
character before this number of bytes), they will be considered equal.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

