###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontSizeDPI

Set font size dynamically with target resolutions (in DPI).

## Header File

Defined in [<SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/SDL2/include/SDL_ttf.h)

## Syntax

```c
int TTF_SetFontSizeDPI(TTF_Font *font, int ptsize, unsigned int hdpi, unsigned int vdpi);
```

## Function Parameters

|                        |            |                            |
| ---------------------- | ---------- | -------------------------- |
| [TTF_Font](TTF_Font) * | **font**   | the font to resize.        |
| int                    | **ptsize** | the new point size.        |
| unsigned int           | **hdpi**   | the target horizontal DPI. |
| unsigned int           | **vdpi**   | the target vertical DPI.   |

## Return Value

(int) Returns 0 if successful, -1 on error.

## Remarks

This clears already-generated glyphs, if any, from the cache.

## Version

This function is available since SDL_ttf 2.0.18.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

