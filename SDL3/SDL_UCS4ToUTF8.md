###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UCS4ToUTF8

Convert a single Unicode codepoint to UTF-8.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
char * SDL_UCS4ToUTF8(Uint32 codepoint, char *dst);
```

## Function Parameters

|        |               |                                                                          |
| ------ | ------------- | ------------------------------------------------------------------------ |
| Uint32 | **codepoint** | a Unicode codepoint to convert to UTF-8.                                 |
| char * | **dst**       | the location to write the encoded UTF-8. Must point to at least 4 bytes! |

## Return Value

(char *) Returns the first byte past the newly-written UTF-8 sequence.

## Remarks

The buffer pointed to by `dst` must be at least 4 bytes long, as this
function may generate between 1 and 4 bytes of output.

This function returns the first byte _after_ the newly-written UTF-8
sequence, which is useful for encoding multiple codepoints in a loop, or
knowing where to write a NULL-terminator character to end the string (in
either case, plan to have a buffer of _more_ than 4 bytes!).

If `codepoint` is an invalid value (outside the Unicode range, or a UTF-16
surrogate value, etc), this will use U+FFFD (REPLACEMENT CHARACTER) for the
codepoint instead, and not set an error.

If `dst` is NULL, this returns NULL immediately without writing to the
pointer and without setting an error.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

