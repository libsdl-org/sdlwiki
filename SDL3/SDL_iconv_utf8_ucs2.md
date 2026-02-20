# SDL_iconv_utf8_ucs2

Convert a UTF-8 string to UCS-2.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_iconv_utf8_ucs2(S)      SDL_reinterpret_cast(Uint16 *, SDL_iconv_string("UCS-2", "UTF-8", S, SDL_strlen(S)+1))
```

## Macro Parameters

|       |                        |
| ----- | ---------------------- |
| **S** | the string to convert. |

## Return Value

Returns a new string, converted to the new encoding, or NULL on error.

## Remarks

This is a helper macro that might be more clear than calling
[SDL_iconv_string](SDL_iconv_string) directly. However, it double-evaluates
its parameter, so do not use an expression with side-effects here.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

