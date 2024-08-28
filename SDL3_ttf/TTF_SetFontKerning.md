###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontKerning

Set if kerning is enabled for a font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
void TTF_SetFontKerning(TTF_Font *font, SDL_bool enabled);
```

## Function Parameters

|                        |             |                                                   |
| ---------------------- | ----------- | ------------------------------------------------- |
| [TTF_Font](TTF_Font) * | **font**    | the font to set kerning on.                       |
| SDL_bool               | **enabled** | SDL_TRUE to enable kerning, SDL_FALSE to disable. |

## Remarks

Newly-opened fonts default to allowing kerning. This is generally a good
policy unless you have a strong reason to disable it, as it tends to
produce better rendering (with kerning disabled, some fonts might render
the word `kerning` as something that looks like `keming` for example).

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

