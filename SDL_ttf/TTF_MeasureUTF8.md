###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_MeasureUTF8

Calculate how much of a UTF-8 string will fit in a given width.

## Syntax

```c
int TTF_MeasureUTF8(TTF_Font *font, const char *text, int measure_width, int *extent, int *count);

```

## Function Parameters

|                       |                                                                   |
| --------------------- | ----------------------------------------------------------------- |
| **font**              | the font to query.                                                |
| **text**              | text to calculate, in UTF-8 encoding.                             |
| **measure_width**     | maximum width, in pixels, available for the string.               |
| **count**             | on return, filled with number of characters that can be rendered. |
| **extent**            | on return, filled with latest calculated width.                   |

## Return Value

Returns 0 if successful, -1 on error.

## Remarks

This reports the number of characters that can be rendered before reaching
`measure_width`.

This does not need to render the string to do this calculation.

## Version

This function is available since SDL_ttf 2.0.18.

## Related Functions

* [TTF_MeasureText](TTF_MeasureText)
* [TTF_MeasureUTF8](TTF_MeasureUTF8)
* [TTF_MeasureUNICODE](TTF_MeasureUNICODE)

----
[CategoryAPI](CategoryAPI)

