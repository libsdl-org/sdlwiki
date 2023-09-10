###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontHinting

Query a font's current FreeType hinter setting.

## Syntax

```c
int TTF_GetFontHinting(const TTF_Font *font);

```

## Function Parameters

|              |                    |
| ------------ | ------------------ |
| **font**     | the font to query. |

## Return Value

Returns the font's current hinter value.

## Remarks

The hinter setting is a single value:

- [`TTF_HINTING_NORMAL`](TTF_HINTING_NORMAL)
- [`TTF_HINTING_LIGHT`](TTF_HINTING_LIGHT)
- [`TTF_HINTING_MONO`](TTF_HINTING_MONO)
- [`TTF_HINTING_NONE`](TTF_HINTING_NONE)
- [`TTF_HINTING_LIGHT_SUBPIXEL`](TTF_HINTING_LIGHT_SUBPIXEL) (available in
  SDL_ttf 3.0.0 and later)

## Version

This function is available since SDL_ttf 3.0.0.

## Related Functions

* [TTF_SetFontHinting](TTF_SetFontHinting)

----
[CategoryAPI](CategoryAPI)

