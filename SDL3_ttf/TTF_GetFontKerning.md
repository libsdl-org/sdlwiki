###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontKerning

Query whether or not kerning is enabled for a font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
SDL_bool TTF_GetFontKerning(const TTF_Font *font);
```

## Function Parameters

|                              |          |                    |
| ---------------------------- | -------- | ------------------ |
| const [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

(SDL_bool) Returns SDL_TRUE if kerning is enabled, SDL_FALSE otherwise.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

