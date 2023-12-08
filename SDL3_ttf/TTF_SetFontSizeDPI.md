###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontSizeDPI

Set font size dynamically with target resolutions (in DPI).

## Syntax

```c
int TTF_SetFontSizeDPI(TTF_Font *font, int ptsize, unsigned int hdpi, unsigned int vdpi);

```

## Function Parameters

|                |                            |
| -------------- | -------------------------- |
| **font**       | the font to resize.        |
| **ptsize**     | the new point size.        |
| **hdpi**       | the target horizontal DPI. |
| **vdpi**       | the target vertical DPI.   |

## Return Value

Returns 0 if successful, -1 on error.

## Remarks

This clears already-generated glyphs, if any, from the cache.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
