###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontSize

Set a font's size dynamically.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
SDL_bool TTF_SetFontSize(TTF_Font *font, int ptsize);
```

## Function Parameters

|                        |            |                     |
| ---------------------- | ---------- | ------------------- |
| [TTF_Font](TTF_Font) * | **font**   | the font to resize. |
| int                    | **ptsize** | the new point size. |

## Return Value

(SDL_bool) Returns SDL_TRUE on success or SDL_FALSE on failure; call
SDL_GetError() for more information.

## Remarks

This clears already-generated glyphs, if any, from the cache.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

