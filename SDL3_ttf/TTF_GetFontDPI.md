###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontDPI

Get font target resolutions, in dots per inch.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetFontDPI(TTF_Font *font, int *hdpi, int *vdpi);
```

## Function Parameters

|                        |          |                                                     |
| ---------------------- | -------- | --------------------------------------------------- |
| [TTF_Font](TTF_Font) * | **font** | the font to query.                                  |
| int *                  | **hdpi** | a pointer filled in with the target horizontal DPI. |
| int *                  | **vdpi** | a pointer filled in with the target vertical DPI.   |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_SetFontSizeDPI](TTF_SetFontSizeDPI)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

