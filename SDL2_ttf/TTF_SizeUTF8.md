###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SizeUTF8

Calculate the dimensions of a rendered string of UTF-8 text.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
int TTF_SizeUTF8(TTF_Font *font, const char *text, int *w, int *h);

```

## Function Parameters

|              |                                                   |
| ------------ | ------------------------------------------------- |
| **font**     | the font to query.                                |
| **text**     | text to calculate, in UTF-8 encoding.             |
| **w**        | will be filled with width, in pixels, on return.  |
| **h**        | will be filled with height, in pixels, on return. |

## Return Value

Returns 0 if successful, -1 on error.

## Remarks

This will report the width and height, in pixels, of the space that the
specified string will take to fully render.

This does not need to render the string to do this calculation.

## Version

This function is available since SDL_ttf 2.0.12.

## See Also

- [TTF_SizeUNICODE](TTF_SizeUNICODE)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

