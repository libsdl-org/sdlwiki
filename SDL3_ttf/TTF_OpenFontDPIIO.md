###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_OpenFontDPIIO

Opens a font from an SDL_IOStream with target resolutions (in DPI).

## Syntax

```c
TTF_Font * TTF_OpenFontDPIIO(SDL_IOStream *src, SDL_bool closeio, int ptsize, unsigned int hdpi, unsigned int vdpi);

```

## Function Parameters

|                 |                                                                              |
| --------------- | ---------------------------------------------------------------------------- |
| **src**         | an SDL_IOStream to provide a font file's data.                               |
| **closeio**     | SDL_TRUE to close `src` when the font is closed, SDL_FALSE to leave it open. |
| **ptsize**      | point size to use for the newly-opened font.                                 |
| **hdpi**        | the target horizontal DPI.                                                   |
| **vdpi**        | the target vertical DPI.                                                     |

## Return Value

Returns a valid [TTF_Font](TTF_Font), or NULL on error.

## Remarks

DPI scaling only applies to scalable fonts (e.g. TrueType).

Some .fon fonts will have several sizes embedded in the file, so the point
size becomes the index of choosing which size. If the value is too high,
the last indexed size will be the default.

If `closeio` is SDL_TRUE `src` will be automatically closed once the font
is closed. Otherwise you should close `src` yourself after closing the
font.

When done with the returned [TTF_Font](TTF_Font), use
[TTF_CloseFont](TTF_CloseFont)() to dispose of it.

## Version

This function is available since SDL_ttf 3.0.0.

## Related Functions

* [TTF_CloseFont](TTF_CloseFont)

----
[CategoryAPI](CategoryAPI)

