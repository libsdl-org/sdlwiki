###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderUTF8_Shaded_Wrapped

Render word-wrapped UTF-8 text at high quality to a new 8-bit surface.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
SDL_Surface * TTF_RenderUTF8_Shaded_Wrapped(TTF_Font *font,
                const char *text, SDL_Color fg, SDL_Color bg, Uint32 wrapLength);
```

## Function Parameters

|                        |          |                                    |
| ---------------------- | -------- | ---------------------------------- |
| [TTF_Font](TTF_Font) * | **font** | the font to render with.           |
| const char *           | **text** | text to render, in UTF-8 encoding. |
| SDL_Color              | **fg**   | the foreground color for the text. |

## Return Value

(SDL_Surface *) Returns a new 8-bit, palettized surface, or NULL if there
was an error.

## Remarks

This function will allocate a new 8-bit, palettized surface. The surface's
0 pixel will be the specified background color, while other pixels have
varying degrees of the foreground color. This function returns the new
surface, or NULL if there was an error.

Text is wrapped to multiple lines on line endings and on word boundaries if
it extends beyond `wrapLength` in pixels.

If wrapLength is 0, this function will only wrap on newline characters.

You can render at other quality levels with
[TTF_RenderUTF8_Solid_Wrapped](TTF_RenderUTF8_Solid_Wrapped),
[TTF_RenderUTF8_Blended_Wrapped](TTF_RenderUTF8_Blended_Wrapped), and
[TTF_RenderUTF8_LCD_Wrapped](TTF_RenderUTF8_LCD_Wrapped).

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_RenderUTF8_Solid_Wrapped](TTF_RenderUTF8_Solid_Wrapped)
- [TTF_RenderUTF8_Blended_Wrapped](TTF_RenderUTF8_Blended_Wrapped)
- [TTF_RenderUTF8_LCD_Wrapped](TTF_RenderUTF8_LCD_Wrapped)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

