###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontSize

Set a font's size dynamically.

## Syntax

```c
int TTF_SetFontSize(TTF_Font *font, int ptsize);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **font**       | the font to resize. |
| **ptsize**     | the new point size. |

## Return Value

Returns 0 if successful, -1 on error

## Remarks

This clears already-generated glyphs, if any, from the cache.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI)

