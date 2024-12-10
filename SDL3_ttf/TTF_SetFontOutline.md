###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontOutline

Set a font's current outline.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetFontOutline(TTF_Font *font, int outline);
```

## Function Parameters

|                        |             |                                       |
| ---------------------- | ----------- | ------------------------------------- |
| [TTF_Font](TTF_Font) * | **font**    | the font to set a new outline on.     |
| int                    | **outline** | positive outline value, 0 to default. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

This uses the font properties
[`TTF_PROP_FONT_OUTLINE_LINE_CAP_NUMBER`](TTF_PROP_FONT_OUTLINE_LINE_CAP_NUMBER),
[`TTF_PROP_FONT_OUTLINE_LINE_JOIN_NUMBER`](TTF_PROP_FONT_OUTLINE_LINE_JOIN_NUMBER),
and
[`TTF_PROP_FONT_OUTLINE_MITER_LIMIT_NUMBER`](TTF_PROP_FONT_OUTLINE_MITER_LIMIT_NUMBER)
when setting the font outline.

This updates any [TTF_Text](TTF_Text) objects using this font, and clears
already-generated glyphs, if any, from the cache.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_GetFontOutline](TTF_GetFontOutline)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

