###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_FontFaceFamilyName

Query a font's family name.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
const char * TTF_FontFaceFamilyName(const TTF_Font *font);
```

## Function Parameters

|                              |          |                    |
| ---------------------------- | -------- | ------------------ |
| const [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

(const char *) Returns the font's family name.

## Remarks

This string is dictated by the contents of the font file.

Note that the returned string is to internal storage, and should not be
modified or free'd by the caller. The string becomes invalid, with the rest
of the font, when `font` is handed to [TTF_CloseFont](TTF_CloseFont)().

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

