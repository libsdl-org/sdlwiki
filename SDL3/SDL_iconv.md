###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_iconv

This function converts text between encodings, reading from and writing to a buffer.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
size_t SDL_iconv(SDL_iconv_t cd, const char **inbuf,
             size_t *inbytesleft, char **outbuf,
             size_t *outbytesleft);
```

## Function Parameters

|                            |                  |                                                                                      |
| -------------------------- | ---------------- | ------------------------------------------------------------------------------------ |
| [SDL_iconv_t](SDL_iconv_t) | **cd**           | The character set conversion context, created in [SDL_iconv_open](SDL_iconv_open)(). |
| const char **              | **inbuf**        | Address of variable that points to the first character of the input sequence.        |
| size_t *                   | **inbytesleft**  | The number of bytes in the input buffer.                                             |
| char **                    | **outbuf**       | Address of variable that points to the output buffer.                                |
| size_t *                   | **outbytesleft** | The number of bytes in the output buffer.                                            |

## Return Value

(size_t) Returns the number of conversions on success, else
[SDL_ICONV_E2BIG](SDL_ICONV_E2BIG) is returned when the output buffer is
too small, or [SDL_ICONV_EILSEQ](SDL_ICONV_EILSEQ) is returned when an
invalid input sequence is encountered, or
[SDL_ICONV_EINVAL](SDL_ICONV_EINVAL) is returned when an incomplete input
sequence is encountered.

On exit:

- inbuf will point to the beginning of the next multibyte
sequence. On error, this is the location of the problematic input sequence.
On success, this is the end of the input sequence. - inbytesleft will be
set to the number of bytes left to convert, which will be 0 on success. 
- outbuf will point to the location where to store the next output byte.
- outbytesleft will be set to the number of bytes left in the output buffer.

## Remarks

It returns the number of succesful conversions.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_iconv_open](SDL_iconv_open)
- [SDL_iconv_close](SDL_iconv_close)
- [SDL_iconv_string](SDL_iconv_string)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

