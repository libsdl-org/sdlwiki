###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_StepBackUTF8

Decode a UTF-8 string in reverse, one Unicode codepoint at a time.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
Uint32 SDL_StepBackUTF8(const char *start, const char **pstr);
```

## Function Parameters

|               |           |                                                              |
| ------------- | --------- | ------------------------------------------------------------ |
| const char *  | **start** | a pointer to the beginning of the UTF-8 string.              |
| const char ** | **pstr**  | a pointer to a UTF-8 string pointer to be read and adjusted. |

## Return Value

(Uint32) Returns the previous Unicode codepoint in the string.

## Remarks

This will go to the start of the previous Unicode codepoint in the string,
move `*pstr` to that location and return that codepoint.

If the resulting codepoint is zero (already at the start of the string), it
will not advance `*pstr` at all.

Generally this function is called in a loop until it returns zero,
adjusting its parameter each iteration.

If an invalid UTF-8 sequence is encountered, this function returns
[SDL_INVALID_UNICODE_CODEPOINT](SDL_INVALID_UNICODE_CODEPOINT).

Several things can generate invalid UTF-8 sequences, including overlong
encodings, the use of UTF-16 surrogate values, and truncated data. Please
refer to
[RFC3629](https://www.ietf.org/rfc/rfc3629.txt)
for details.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.5.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

