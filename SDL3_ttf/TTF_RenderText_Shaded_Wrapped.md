###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderText_Shaded_Wrapped

Render word-wrapped UTF-8 text at high quality to a new 8-bit surface.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
SDL_Surface * TTF_RenderText_Shaded_Wrapped(TTF_Font *font, const char *text, size_t length, SDL_Color fg, SDL_Color bg, int wrap_width);
```

## Function Parameters

|                        |                |                                                                           |
| ---------------------- | -------------- | ------------------------------------------------------------------------- |
| [TTF_Font](TTF_Font) * | **font**       | the font to render with.                                                  |
| const char *           | **text**       | text to render, in UTF-8 encoding.                                        |
| size_t                 | **length**     | the length of the text, in bytes, or 0 for null terminated text.          |
| SDL_Color              | **fg**         | the foreground color for the text.                                        |
| SDL_Color              | **bg**         | the background color for the text.                                        |
| int                    | **wrap_width** | the maximum width of the text surface or 0 to wrap on newline characters. |

## Return Value

(SDL_Surface *) Returns a new 8-bit, palettized surface, or NULL if there
was an error.

## Remarks

This function will allocate a new 8-bit, palettized surface. The surface's
0 pixel will be the specified background color, while other pixels have
varying degrees of the foreground color. This function returns the new
surface, or NULL if there was an error.

Text is wrapped to multiple lines on line endings and on word boundaries if
it extends beyond `wrap_width` in pixels.

If wrap_width is 0, this function will only wrap on newline characters.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_RenderText_Blended_Wrapped](TTF_RenderText_Blended_Wrapped)
- [TTF_RenderText_LCD_Wrapped](TTF_RenderText_LCD_Wrapped)
- [TTF_RenderText_Shaded](TTF_RenderText_Shaded)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

