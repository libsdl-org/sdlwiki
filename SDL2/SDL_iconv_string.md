# SDL_iconv_string

This function converts a buffer or string between encodings in one pass, returning a string that must be freed with [SDL_free](SDL_free)() or NULL on error.

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_stdinc.h)

## Syntax

```c
char* SDL_iconv_string(const char *tocode,
                       const char *fromcode,
                       const char *inbuf,
                       size_t inbytesleft);
```

## Function Parameters

|              |                 |                                                |
| ------------ | --------------- | ---------------------------------------------- |
| const char * | **tocode**      | the character encoding of the output string.   |
| const char * | **fromcode**    | the character encoding of data in `inbuf`.     |
| const char * | **inbuf**       | the string to convert to a different encoding. |
| size_t       | **inbytesleft** | the size of the input string _in bytes_.       |

## Return Value

(char *) Returns a new string, converted to the new encoding, or NULL on
error.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdInc](CategoryStdInc)

