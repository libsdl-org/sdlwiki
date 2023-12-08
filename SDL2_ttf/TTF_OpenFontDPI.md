###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_OpenFontDPI

Create a font from a file, using target resolutions (in DPI).

## Syntax

```c
TTF_Font * TTF_OpenFontDPI(const char *file, int ptsize, unsigned int hdpi, unsigned int vdpi);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **file**       | path to font file.                           |
| **ptsize**     | point size to use for the newly-opened font. |
| **hdpi**       | the target horizontal DPI.                   |
| **vdpi**       | the target vertical DPI.                     |

## Return Value

Returns a valid [TTF_Font](TTF_Font.md), or NULL on error.

## Remarks

DPI scaling only applies to scalable fonts (e.g. TrueType).

Some .fon fonts will have several sizes embedded in the file, so the point
size becomes the index of choosing which size. If the value is too high,
the last indexed size will be the default.

When done with the returned [TTF_Font](TTF_Font.md), use
[TTF_CloseFont](TTF_CloseFont.md)() to dispose of it.

## Version

This function is available since SDL_ttf 2.0.18.

## Related Functions

* [TTF_CloseFont](TTF_CloseFont.md)

----
[CategoryAPI](CategoryAPI.md)
