###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderGlyph_Blended

Render a single 16-bit glyph at high quality to a new ARGB surface.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
SDL_Surface * TTF_RenderGlyph_Blended(TTF_Font *font,
                Uint16 ch, SDL_Color fg);

```

## Function Parameters

|              |                                    |
| ------------ | ---------------------------------- |
| **font**     | the font to render with.           |
| **ch**       | the character to render.           |
| **fg**       | the foreground color for the text. |

## Return Value

Returns a new 32-bit, ARGB surface, or NULL if there was an error.

## Remarks

This function will allocate a new 32-bit, ARGB surface, using alpha
blending to dither the font with the given color. This function returns the
new surface, or NULL if there was an error.

The glyph is rendered without any padding or centering in the X direction,
and aligned normally in the Y direction.

Note that this version of the function takes a 16-bit character code, which
covers the Basic Multilingual Plane, but is insufficient to cover the
entire set of possible Unicode values, including emoji glyphs. You should
use [TTF_RenderGlyph32_Blended](TTF_RenderGlyph32_Blended)() instead, which
offers the same functionality but takes a 32-bit codepoint instead.

The only reason to use this function is that it was available since the
beginning of time, more or less.

You can render at other quality levels with
[TTF_RenderGlyph_Solid](TTF_RenderGlyph_Solid),
[TTF_RenderGlyph_Shaded](TTF_RenderGlyph_Shaded), and
[TTF_RenderGlyph_LCD](TTF_RenderGlyph_LCD).

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

* [TTF_RenderGlyph32_Blended](TTF_RenderGlyph32_Blended)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

