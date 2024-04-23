###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_wcsncmp

Compare two wide strings up to a number of wchar_t values.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_wcsncmp(const wchar_t *str1, const wchar_t *str2, size_t maxlen);

```

## Function Parameters

|                |                                                      |
| -------------- | ---------------------------------------------------- |
| **str1**       | The first string to compare. NULL is not permitted!  |
| **str2**       | The second string to compare. NULL is not permitted! |
| **maxlen**     | The maximum number of wchar_t to compare.            |

## Return Value

Returns less than zero if str1 is "less than" str2, greater than zero if
str1 is "greater than" str2, and zero if the strings match exactly.

## Remarks

This only compares wchar_t values; it does not care if the string is
well-formed UTF-16 (or UTF-32, depending on your platform's wchar_t size),
or uses valid Unicode values.

Note that while this function is intended to be used with UTF-16 (or
UTF-32, depending on your platform's definition of wchar_t), it is
comparing raw wchar_t values and not Unicode codepoints: `maxlen` specifies
a wchar_t limit! If the limit lands in the middle of a multi-wchar UTF-16
sequence, it will only compare a portion of the final character.

`maxlen` specifies a maximum number of wchar_t to compare; if the strings
match to this number of wide chars (or both have matched to a
null-terminator character before this count), they will be considered
equal.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

