###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontHinting

Set a font's current hinter setting.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
void TTF_SetFontHinting(TTF_Font *font, int hinting);
```

## Function Parameters

|                        |             |                                          |
| ---------------------- | ----------- | ---------------------------------------- |
| [TTF_Font](TTF_Font) * | **font**    | the font to set a new hinter setting on. |
| int                    | **hinting** | the new hinter setting.                  |

## Remarks

Setting it clears already-generated glyphs, if any, from the cache.

The hinter setting is a single value:

- [`TTF_HINTING_NORMAL`](TTF_HINTING_NORMAL)
- [`TTF_HINTING_LIGHT`](TTF_HINTING_LIGHT)
- [`TTF_HINTING_MONO`](TTF_HINTING_MONO)
- [`TTF_HINTING_NONE`](TTF_HINTING_NONE)
- [`TTF_HINTING_LIGHT_SUBPIXEL`](TTF_HINTING_LIGHT_SUBPIXEL) (available in
  SDL_ttf 3.0.0 and later)

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_GetFontHinting](TTF_GetFontHinting)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

