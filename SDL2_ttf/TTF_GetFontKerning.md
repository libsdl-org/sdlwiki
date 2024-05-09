###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontKerning

Query whether or not kerning is allowed for a font.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
int TTF_GetFontKerning(const TTF_Font *font);

```

## Function Parameters

|              |                    |
| ------------ | ------------------ |
| **font**     | the font to query. |

## Return Value

Returns non-zero if kerning is enabled, zero otherwise.

## Version

This function is available since SDL_ttf 2.0.12.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

