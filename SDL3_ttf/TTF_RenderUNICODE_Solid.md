###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderUNICODE_Solid

Render UCS-2 text at fast quality to a new 8-bit surface.

## Syntax

```c
SDL_Surface * TTF_RenderUNICODE_Solid(TTF_Font *font,
                const Uint16 *text, SDL_Color fg);

```

## Function Parameters

|              |                                    |
| ------------ | ---------------------------------- |
| **font**     | the font to render with.           |
| **text**     | text to render, in UCS-2 encoding. |
| **fg**       | the foreground color for the text. |

## Return Value

Returns a new 8-bit, palettized surface, or NULL if there was an error.

## Remarks

This function will allocate a new 8-bit, palettized surface. The surface's
0 pixel will be the colorkey, giving a transparent background. The 1 pixel
will be set to the text color.

This will not word-wrap the string; you'll get a surface with a single line
of text, as long as the string requires. You can use
[TTF_RenderUNICODE_Solid_Wrapped](TTF_RenderUNICODE_Solid_Wrapped)()
instead if you need to wrap the output to multiple lines.

This will not wrap on newline characters.

Please note that this function is named "Unicode" but currently expects
UCS-2 encoding (16 bits per codepoint). This does not give you access to
large Unicode values, such as emoji glyphs. These codepoints are accessible
through the UTF-8 version of this function.

You can render at other quality levels with
[TTF_RenderUNICODE_Shaded](TTF_RenderUNICODE_Shaded),
[TTF_RenderUNICODE_Blended](TTF_RenderUNICODE_Blended), and
[TTF_RenderUNICODE_LCD](TTF_RenderUNICODE_LCD).

## Version

This function is available since SDL_ttf 2.0.12.

## Related Functions

* [TTF_RenderUTF8_Solid](TTF_RenderUTF8_Solid)

----
[CategoryAPI](CategoryAPI)

