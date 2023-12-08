###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SizeUNICODE

Calculate the dimensions of a rendered string of UCS-2 text.

## Syntax

```c
int TTF_SizeUNICODE(TTF_Font *font, const Uint16 *text, int *w, int *h);

```

## Function Parameters

|              |                                                   |
| ------------ | ------------------------------------------------- |
| **font**     | the font to query.                                |
| **text**     | text to calculate, in UCS-2 encoding.             |
| **w**        | will be filled with width, in pixels, on return.  |
| **h**        | will be filled with height, in pixels, on return. |

## Return Value

Returns 0 if successful, -1 on error.

## Remarks

This will report the width and height, in pixels, of the space that the
specified string will take to fully render.

This does not need to render the string to do this calculation.

Please note that this function is named "Unicode" but currently expects
UCS-2 encoding (16 bits per codepoint). This does not give you access to
large Unicode values, such as emoji glyphs. These codepoints are accessible
through the UTF-8 version of this function.

## Version

This function is available since SDL_ttf 3.0.0.

## Related Functions

* [TTF_SizeUTF8](TTF_SizeUTF8.md)

----
[CategoryAPI](CategoryAPI.md)
