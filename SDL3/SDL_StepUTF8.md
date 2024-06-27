###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_StepUTF8

Decode a UTF-8 string, one Unicode codepoint at a time.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
Uint32 SDL_StepUTF8(const char **pstr, size_t *pslen);
```

## Function Parameters

|               |           |                                                                                           |
| ------------- | --------- | ----------------------------------------------------------------------------------------- |
| const char ** | **pstr**  | a pointer to a UTF-8 string pointer to be read and adjusted.                              |
| size_t *      | **pslen** | a pointer to the number of bytes in the string, to be read and adjusted. NULL is allowed. |

## Return Value

(Uint32) Returns the first Unicode codepoint in the string.

## Remarks

This will return the first Unicode codepoint in the UTF-8 encoded string in
`*pstr`, and then advance `*pstr` past any consumed bytes before returning.

It will not access more than `*pslen` bytes from the string. `*pslen` will
be adjusted, as well, subtracting the number of bytes consumed.

`pslen` is allowed to be NULL, in which case the string _must_ be
NULL-terminated, as the function will blindly read until it sees the NULL
char.

if `*pslen` is zero, it assumes the end of string is reached and returns a
zero codepoint regardless of the contents of the string buffer.

If the resulting codepoint is zero (a NULL terminator), or `*pslen` is
zero, it will not advance `*pstr` or `*pslen` at all.

Generally this function is called in a loop until it returns zero,
adjusting its parameters each iteration.

If an invalid UTF-8 sequence is encountered, this function returns
[SDL_INVALID_UNICODE_CODEPOINT](SDL_INVALID_UNICODE_CODEPOINT) and advances
the string/length by one byte (which is to say, a multibyte sequence might
produce several
[SDL_INVALID_UNICODE_CODEPOINT](SDL_INVALID_UNICODE_CODEPOINT) returns
before it syncs to the next valid UTF-8 sequence).

Several things can generate invalid UTF-8 sequences, including overlong
encodings, the use of UTF-16 surrogate values, and truncated data. Please
refer to
[RFC3629](https://www.ietf.org/rfc/rfc3629.txt)
for details.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

