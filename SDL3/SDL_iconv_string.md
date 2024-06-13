###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_iconv_string

Helper function to convert a string's encoding in one call.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
char* SDL_iconv_string(const char *tocode,
                   const char *fromcode,
                   const char *inbuf,
                   size_t inbytesleft);
```

## Function Parameters

|              |                 |                                                                                  |
| ------------ | --------------- | -------------------------------------------------------------------------------- |
| const char * | **tocode**      | the character encoding of the output string. Examples are "UTF-8", "UCS-4", etc. |
| const char * | **fromcode**    | the character encoding of data in `inbuf`.                                       |
| const char * | **inbuf**       | the string to convert to a different encoding.                                   |
| size_t       | **inbytesleft** | the size of the input string _in bytes_.                                         |

## Return Value

(char *) Returns a new string, converted to the new encoding, or NULL on
error.

## Remarks

This function converts a buffer or string between encodings in one pass.

The string does not need to be NULL-terminated; this function operates on
the number of bytes specified in `inbytesleft` whether there is a NULL
character anywhere in the buffer.

The returned string is owned by the caller, and should be passed to
[SDL_free](SDL_free) when no longer needed.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

