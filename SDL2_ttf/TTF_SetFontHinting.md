###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontHinting

Set a font's current hinter setting.

## Syntax

```c
void TTF_SetFontHinting(TTF_Font *font, int hinting);

```

## Function Parameters

|                 |                                          |
| --------------- | ---------------------------------------- |
| **font**        | the font to set a new hinter setting on. |
| **hinting**     | the new hinter setting.                  |

## Remarks

Setting it clears already-generated glyphs, if any, from the cache.

The hinter setting is a single value:

- [`TTF_HINTING_NORMAL`](TTF_HINTING_NORMAL)
- [`TTF_HINTING_LIGHT`](TTF_HINTING_LIGHT)
- [`TTF_HINTING_MONO`](TTF_HINTING_MONO)
- [`TTF_HINTING_NONE`](TTF_HINTING_NONE)
- [`TTF_HINTING_LIGHT_SUBPIXEL`](TTF_HINTING_LIGHT_SUBPIXEL) (available in
  SDL_ttf 2.0.18 and later)

## Version

This function is available since SDL_ttf 2.0.12.

## Related Functions

* [TTF_GetFontHinting](TTF_GetFontHinting.md)

----
[CategoryAPI](CategoryAPI.md)
