###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_iconv_close

This function frees a context used for character set conversion.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_iconv_close(SDL_iconv_t cd);
```

## Function Parameters

|                            |        |                                      |
| -------------------------- | ------ | ------------------------------------ |
| [SDL_iconv_t](SDL_iconv_t) | **cd** | The character set conversion handle. |

## Return Value

(int) Returns 0 on success, or -1 on failure.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_iconv](SDL_iconv)
- [SDL_iconv_open](SDL_iconv_open)
- [SDL_iconv_string](SDL_iconv_string)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

