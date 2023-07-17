###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_FontFaceStyleName

Query a font's style name.

## Syntax

```c
const char * TTF_FontFaceStyleName(const TTF_Font *font);

```

## Function Parameters

|              |                    |
| ------------ | ------------------ |
| **font**     | the font to query. |

## Return Value

Returns the font's style name.

## Remarks

This string is dictated by the contents of the font file.

Note that the returned string is to internal storage, and should not be
modified or free'd by the caller. The string becomes invalid, with the rest
of the font, when `font` is handed to [TTF_CloseFont](TTF_CloseFont)().

## Version

This function is available since SDL_ttf 2.0.12.

----
[CategoryAPI](CategoryAPI)

