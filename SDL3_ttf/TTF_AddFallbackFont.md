###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_AddFallbackFont

Add a fallback font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_AddFallbackFont(TTF_Font *font, TTF_Font *fallback);
```

## Function Parameters

|                        |              |                                |
| ---------------------- | ------------ | ------------------------------ |
| [TTF_Font](TTF_Font) * | **font**     | the font to modify.            |
| [TTF_Font](TTF_Font) * | **fallback** | the font to add as a fallback. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

Add a font that will be used for glyphs that are not in the current font.
The fallback font should have the same size and style as the current font.

If there are multiple fallback fonts, they are used in the order added.

This updates any [TTF_Text](TTF_Text) objects using this font.

## Thread Safety

This function should be called on the thread that created both fonts.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_ClearFallbackFonts](TTF_ClearFallbackFonts)
- [TTF_RemoveFallbackFont](TTF_RemoveFallbackFont)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

