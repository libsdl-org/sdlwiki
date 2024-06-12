###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SizeUNICODE

Calculate the dimensions of a rendered string of UCS-2 text.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
int TTF_SizeUNICODE(TTF_Font *font, const Uint16 *text, int *w, int *h);
```

## Function Parameters

|                        |          |                                                   |
| ---------------------- | -------- | ------------------------------------------------- |
| [TTF_Font](TTF_Font) * | **font** | the font to query.                                |
| const Uint16 *         | **text** | text to calculate, in UCS-2 encoding.             |
| int *                  | **w**    | will be filled with width, in pixels, on return.  |
| int *                  | **h**    | will be filled with height, in pixels, on return. |

## Return Value

(int) Returns 0 if successful, -1 on error.

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

## See Also

- [TTF_SizeUTF8](TTF_SizeUTF8)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

