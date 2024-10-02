###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontWrapAlignment

Set a font's current wrap alignment option.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
void TTF_SetFontWrapAlignment(TTF_Font *font, TTF_HorizontalAlignment align);
```

## Function Parameters

|                                                    |           |                                                 |
| -------------------------------------------------- | --------- | ----------------------------------------------- |
| [TTF_Font](TTF_Font) *                             | **font**  | the font to set a new wrap alignment option on. |
| [TTF_HorizontalAlignment](TTF_HorizontalAlignment) | **align** | the new wrap alignment option.                  |

## Remarks

This updates any [TTF_Text](TTF_Text) objects using this font.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_GetFontWrapAlignment](TTF_GetFontWrapAlignment)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

