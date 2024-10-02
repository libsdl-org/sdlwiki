###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontSize

Set a font's size dynamically.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetFontSize(TTF_Font *font, float ptsize);
```

## Function Parameters

|                        |            |                     |
| ---------------------- | ---------- | ------------------- |
| [TTF_Font](TTF_Font) * | **font**   | the font to resize. |
| float                  | **ptsize** | the new point size. |

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

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

