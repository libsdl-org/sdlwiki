# SDL_wcscasecmp

Compare two null-terminated wide strings, case-insensitively.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_wcscasecmp(const wchar_t *str1, const wchar_t *str2);
```

## Function Parameters

|                 |          |                                                      |
| --------------- | -------- | ---------------------------------------------------- |
| const wchar_t * | **str1** | the first string to compare. NULL is not permitted!  |
| const wchar_t * | **str2** | the second string to compare. NULL is not permitted! |

## Return Value

(int) Returns less than zero if str1 is "less than" str2, greater than zero
if str1 is "greater than" str2, and zero if the strings match exactly.

## Remarks

This will work with Unicode strings, using a technique called
"case-folding" to handle the vast majority of case-sensitive human
languages regardless of system locale. It can deal with expanding values: a
German Eszett character can compare against two ASCII 's' chars and be
considered a match, for example. A notable exception: it does not handle
the Turkish 'i' character; human language is complicated!

Depending on your platform, "wchar_t" might be 2 bytes, and expected to be
UTF-16 encoded (like Windows), or 4 bytes in UTF-32 format. Since this
handles Unicode, it expects the string to be well-formed and not a
null-terminated string of arbitrary bytes. Characters that are not valid
UTF-16 (or UTF-32) are treated as Unicode character U+FFFD (REPLACEMENT
CHARACTER), which is to say two strings of random bits may turn out to
match if they convert to the same amount of replacement characters.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

