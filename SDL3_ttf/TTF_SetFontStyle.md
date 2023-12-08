###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontStyle

Set a font's current style.

## Syntax

```c
void TTF_SetFontStyle(TTF_Font *font, int style);

```

## Function Parameters

|               |                                             |
| ------------- | ------------------------------------------- |
| **font**      | the font to set a new style on.             |
| **style**     | the new style values to set, OR'd together. |

## Remarks

Setting the style clears already-generated glyphs, if any, from the cache.

The font styles are a set of bit flags, OR'd together:

- [`TTF_STYLE_NORMAL`](TTF_STYLE_NORMAL) (is zero)
- [`TTF_STYLE_BOLD`](TTF_STYLE_BOLD)
- [`TTF_STYLE_ITALIC`](TTF_STYLE_ITALIC)
- [`TTF_STYLE_UNDERLINE`](TTF_STYLE_UNDERLINE)
- [`TTF_STYLE_STRIKETHROUGH`](TTF_STYLE_STRIKETHROUGH)

## Version

This function is available since SDL_ttf 3.0.0.

## Related Functions

* [TTF_GetFontStyle](TTF_GetFontStyle.md)

----
[CategoryAPI](CategoryAPI.md)
