###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontSizeDPI

Set font size dynamically with target resolutions, in dots per inch.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetFontSizeDPI(TTF_Font *font, float ptsize, int hdpi, int vdpi);
```

## Function Parameters

|                        |            |                            |
| ---------------------- | ---------- | -------------------------- |
| [TTF_Font](TTF_Font) * | **font**   | the font to resize.        |
| float                  | **ptsize** | the new point size.        |
| int                    | **hdpi**   | the target horizontal DPI. |
| int                    | **vdpi**   | the target vertical DPI.   |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

This updates any [TTF_Text](TTF_Text) objects using this font, and clears
already-generated glyphs, if any, from the cache.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_GetFontSize](TTF_GetFontSize)
- [TTF_GetFontSizeDPI](TTF_GetFontSizeDPI)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

