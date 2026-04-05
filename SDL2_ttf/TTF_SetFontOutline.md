###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontOutline

Set a font's current outline.

## Header File

Defined in [<SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/SDL2/include/SDL_ttf.h)

## Syntax

```c
void TTF_SetFontOutline(TTF_Font *font, int outline);
```

## Function Parameters

|                        |             |                                       |
| ---------------------- | ----------- | ------------------------------------- |
| [TTF_Font](TTF_Font) * | **font**    | the font to set a new outline on.     |
| int                    | **outline** | positive outline value, 0 to default. |

## Version

This function is available since SDL_ttf 2.0.12.

## See Also

- [TTF_GetFontOutline](TTF_GetFontOutline)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

