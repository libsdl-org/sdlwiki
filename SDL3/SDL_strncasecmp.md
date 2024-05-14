###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_strncasecmp

Compare two UTF-8 strings, case-insensitively, up to a number of bytes.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_strncasecmp(const char *str1, const char *str2, size_t maxlen);

```

## Function Parameters

|                |                                                      |
| -------------- | ---------------------------------------------------- |
| **str1**       | The first string to compare. NULL is not permitted!  |
| **str2**       | The second string to compare. NULL is not permitted! |
| **maxlen**     | The maximum number of bytes to compare.              |

## Return Value

Returns less than zero if str1 is "less than" str2, greater than zero if
str1 is "greater than" str2, and zero if the strings match exactly.

## Remarks

This will work with Unicode strings, using a technique called
"case-folding" to handle the vast majority of case-sensitive human
languages regardless of system locale. It can deal with expanding values: a
German Eszett character can compare against two ASCII 's' chars and be
considered a match, for example. A notable exception: it does not handle
the Turkish 'i' character; human language is complicated!

Since this handles Unicode, it expects the string to be well-formed UTF-8
and not a null-terminated string of arbitrary bytes. Bytes that are not
valid UTF-8 are treated as Unicode character U+FFFD (REPLACEMENT
CHARACTER), which is to say two strings of random bits may turn out to
match if they convert to the same amount of replacement characters.

Note that while this function is intended to be used with UTF-8, `maxlen`
specifies a _byte_ limit! If the limit lands in the middle of a multi-byte
UTF-8 sequence, it may convert a portion of the final character to one or
more Unicode character U+FFFD (REPLACEMENT CHARACTER) so as not to overflow
a buffer.

`maxlen` specifies a maximum number of bytes to compare; if the strings
match to this number of bytes (or both have matched to a null-terminator
character before this number of bytes), they will be considered equal.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

