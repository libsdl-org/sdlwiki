###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderUTF8_Shaded

Render UTF-8 text at high quality to a new 8-bit surface.

## Syntax

```c
SDL_Surface * TTF_RenderUTF8_Shaded(TTF_Font *font,
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

Returns a new 8-bit, palettized surface, or NULL if there was an error.

## Remarks

This function will allocate a new 8-bit, palettized surface. The surface's
0 pixel will be the specified background color, while other pixels have
varying degrees of the foreground color. This function returns the new
surface, or NULL if there was an error.

This will not word-wrap the string; you'll get a surface with a single line
of text, as long as the string requires. You can use
[TTF_RenderUTF8_Shaded_Wrapped](TTF_RenderUTF8_Shaded_Wrapped)() instead if
you need to wrap the output to multiple lines.

This will not wrap on newline characters.

You can render at other quality levels with
[TTF_RenderUTF8_Solid](TTF_RenderUTF8_Solid),
[TTF_RenderUTF8_Blended](TTF_RenderUTF8_Blended), and
[TTF_RenderUTF8_LCD](TTF_RenderUTF8_LCD).

## Version

This function is available since SDL_ttf 3.0.0.

## Related Functions

* [TTF_RenderUNICODE_Shaded](TTF_RenderUNICODE_Shaded)

----
[CategoryAPI](CategoryAPI)

