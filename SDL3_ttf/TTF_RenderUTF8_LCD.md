###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderUTF8_LCD

Render UTF-8 text at LCD subpixel quality to a new ARGB surface.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
SDL_Surface * TTF_RenderUTF8_LCD(TTF_Font *font,
                const char *text, SDL_Color fg, SDL_Color bg);

```

## Function Parameters

|              |                                    |
| ------------ | ---------------------------------- |
| **font**     | the font to render with.           |
| **text**     | text to render, in UTF-8 encoding. |
| **fg**       | the foreground color for the text. |
| **bg**       | the background color for the text. |

## Return Value

Returns a new 32-bit, ARGB surface, or NULL if there was an error.

## Remarks

This function will allocate a new 32-bit, ARGB surface, and render
alpha-blended text using FreeType's LCD subpixel rendering. This function
returns the new surface, or NULL if there was an error.

This will not word-wrap the string; you'll get a surface with a single line
of text, as long as the string requires. You can use
[TTF_RenderUTF8_LCD_Wrapped](TTF_RenderUTF8_LCD_Wrapped)() instead if you
need to wrap the output to multiple lines.

This will not wrap on newline characters.

You can render at other quality levels with
[TTF_RenderUTF8_Solid](TTF_RenderUTF8_Solid),
[TTF_RenderUTF8_Shaded](TTF_RenderUTF8_Shaded), and
[TTF_RenderUTF8_Blended](TTF_RenderUTF8_Blended).

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_RenderUNICODE_LCD](TTF_RenderUNICODE_LCD)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

