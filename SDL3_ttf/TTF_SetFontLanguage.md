###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontLanguage

Set language to be used for text shaping by a font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetFontLanguage(TTF_Font *font, const char *language_bcp47);
```

## Function Parameters

|                        |                    |                                                                                                    |
| ---------------------- | ------------------ | -------------------------------------------------------------------------------------------------- |
| [TTF_Font](TTF_Font) * | **font**           | the font to specify a language for.                                                                |
| const char *           | **language_bcp47** | a null-terminated string containing the desired language's BCP47 code. Or null to reset the value. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

If SDL_ttf was not built with HarfBuzz support, this function returns
false.

This updates any [TTF_Text](TTF_Text) objects using this font.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

