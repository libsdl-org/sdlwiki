###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontOutline

Query a font's current outline.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
int TTF_GetFontOutline(const TTF_Font *font);
```

## Function Parameters

|                              |          |                    |
| ---------------------------- | -------- | ------------------ |
| const [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

(int) Returns the font's current outline value.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_SetFontOutline](TTF_SetFontOutline)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

