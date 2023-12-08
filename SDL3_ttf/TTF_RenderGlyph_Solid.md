###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderGlyph_Solid

Render a single 16-bit glyph at fast quality to a new 8-bit surface.

## Syntax

```c
SDL_Surface * TTF_RenderGlyph_Solid(TTF_Font *font,
                Uint16 ch, SDL_Color fg);

```

## Function Parameters

|              |                                    |
| ------------ | ---------------------------------- |
| **font**     | the font to render with.           |
| **ch**       | the character to render.           |
| **fg**       | the foreground color for the text. |

## Return Value

Returns a new 8-bit, palettized surface, or NULL if there was an error.

## Remarks

This function will allocate a new 8-bit, palettized surface. The surface's
0 pixel will be the colorkey, giving a transparent background. The 1 pixel
will be set to the text color.

The glyph is rendered without any padding or centering in the X direction,
and aligned normally in the Y direction.

Note that this version of the function takes a 16-bit character code, which
covers the Basic Multilingual Plane, but is insufficient to cover the
entire set of possible Unicode values, including emoji glyphs. You should
use [TTF_RenderGlyph32_Solid](TTF_RenderGlyph32_Solid.md)() instead, which
offers the same functionality but takes a 32-bit codepoint instead.

The only reason to use this function is that it was available since the
beginning of time, more or less.

You can render at other quality levels with
[TTF_RenderGlyph_Shaded](TTF_RenderGlyph_Shaded.md),
[TTF_RenderGlyph_Blended](TTF_RenderGlyph_Blended.md), and
[TTF_RenderGlyph_LCD](TTF_RenderGlyph_LCD.md).

## Version

This function is available since SDL_ttf 3.0.0.

## Related Functions

* [TTF_RenderGlyph32_Solid](TTF_RenderGlyph32_Solid.md)

----
[CategoryAPI](CategoryAPI.md)
