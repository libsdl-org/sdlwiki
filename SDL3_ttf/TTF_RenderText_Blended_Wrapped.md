###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderText_Blended_Wrapped

Render word-wrapped UTF-8 text at high quality to a new ARGB surface.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
SDL_Surface * TTF_RenderText_Blended_Wrapped(TTF_Font *font, const char *text, size_t length, SDL_Color fg, int wrap_width);
```

## Function Parameters

|                        |                |                                                                           |
| ---------------------- | -------------- | ------------------------------------------------------------------------- |
| [TTF_Font](TTF_Font) * | **font**       | the font to render with.                                                  |
| const char *           | **text**       | text to render, in UTF-8 encoding.                                        |
| size_t                 | **length**     | the length of the text, in bytes, or 0 for null terminated text.          |
| SDL_Color              | **fg**         | the foreground color for the text.                                        |
| int                    | **wrap_width** | the maximum width of the text surface or 0 to wrap on newline characters. |

## Return Value

(SDL_Surface *) Returns a new 32-bit, ARGB surface, or NULL if there was an
error.

## Remarks

This function will allocate a new 32-bit, ARGB surface, using alpha
blending to dither the font with the given color. This function returns the
new surface, or NULL if there was an error.

Text is wrapped to multiple lines on line endings and on word boundaries if
it extends beyond `wrap_width` in pixels.

If wrap_width is 0, this function will only wrap on newline characters.

You can render at other quality levels with
[TTF_RenderText_Solid_Wrapped](TTF_RenderText_Solid_Wrapped),
[TTF_RenderText_Shaded_Wrapped](TTF_RenderText_Shaded_Wrapped), and
[TTF_RenderText_LCD_Wrapped](TTF_RenderText_LCD_Wrapped).

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_RenderText_Blended](TTF_RenderText_Blended)
- [TTF_RenderText_LCD_Wrapped](TTF_RenderText_LCD_Wrapped)
- [TTF_RenderText_Shaded_Wrapped](TTF_RenderText_Shaded_Wrapped)
- [TTF_RenderText_Solid_Wrapped](TTF_RenderText_Solid_Wrapped)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

