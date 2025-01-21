###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_iconv_open

This function allocates a context for the specified character set conversion.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
SDL_iconv_t SDL_iconv_open(const char *tocode,
                       const char *fromcode);
```

## Function Parameters

|              |              |                                                  |
| ------------ | ------------ | ------------------------------------------------ |
| const char * | **tocode**   | The target character encoding, must not be NULL. |
| const char * | **fromcode** | The source character encoding, must not be NULL. |

## Return Value

([SDL_iconv_t](SDL_iconv_t)) Returns a handle that must be freed with
[SDL_iconv_close](SDL_iconv_close), or [SDL_ICONV_ERROR](SDL_ICONV_ERROR)
on failure.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_iconv](SDL_iconv)
- [SDL_iconv_close](SDL_iconv_close)
- [SDL_iconv_string](SDL_iconv_string)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

