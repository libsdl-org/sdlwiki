###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderText_Shaded

Render Latin1 text at high quality to a new 8-bit surface.

## Syntax

```c
SDL_Surface * TTF_RenderText_Shaded(TTF_Font *font,
                const char *text, SDL_Color fg, SDL_Color bg);

```

## Function Parameters

|              |                                     |
| ------------ | ----------------------------------- |
| **font**     | the font to render with.            |
| **text**     | text to render, in Latin1 encoding. |
| **fg**       | the foreground color for the text.  |
| **bg**       | the background color for the text.  |

## Return Value

Returns a new 8-bit, palettized surface, or NULL if there was an error.

## Remarks

This function will allocate a new 8-bit, palettized surface. The surface's
0 pixel will be the specified background color, while other pixels have
varying degrees of the foreground color. This function returns the new
surface, or NULL if there was an error.

This will not word-wrap the string; you'll get a surface with a single line
of text, as long as the string requires. You can use
[TTF_RenderText_Shaded_Wrapped](TTF_RenderText_Shaded_Wrapped.md)() instead if
you need to wrap the output to multiple lines.

This will not wrap on newline characters.

You almost certainly want [TTF_RenderUTF8_Shaded](TTF_RenderUTF8_Shaded.md)()
unless you're sure you have a 1-byte Latin1 encoding. US ASCII characters
will work with either function, but most other Unicode characters packed
into a `const char *` will need UTF-8.

You can render at other quality levels with
[TTF_RenderText_Solid](TTF_RenderText_Solid.md),
[TTF_RenderText_Blended](TTF_RenderText_Blended.md), and
[TTF_RenderText_LCD](TTF_RenderText_LCD.md).

## Version

This function is available since SDL_ttf 3.0.0.

## Related Functions

* [TTF_RenderUTF8_Shaded](TTF_RenderUTF8_Shaded.md)
* [TTF_RenderUNICODE_Shaded](TTF_RenderUNICODE_Shaded.md)

----
[CategoryAPI](CategoryAPI.md)
