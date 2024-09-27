###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontScript

Set script to be used for text shaping by a font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetFontScript(TTF_Font *font, const char *script);
```

## Function Parameters

|                        |            |                                                 |
| ---------------------- | ---------- | ----------------------------------------------- |
| [TTF_Font](TTF_Font) * | **font**   | the font to specify a script name for.          |
| const char *           | **script** | null-terminated string of exactly 4 characters. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

The supplied script value must be a null-terminated string of exactly four
characters.

If SDL_ttf was not built with HarfBuzz support, this function returns
false.

## Thread Safety

This function is not thread-safe.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

