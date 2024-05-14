###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderGlyph_LCD

Render a single 16-bit glyph at LCD subpixel quality to a new ARGB surface.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
SDL_Surface * TTF_RenderGlyph_LCD(TTF_Font *font,
                Uint16 ch, SDL_Color fg, SDL_Color bg);

```

## Function Parameters

|              |                                    |
| ------------ | ---------------------------------- |
| **font**     | the font to render with.           |
| **ch**       | the character to render.           |
| **fg**       | the foreground color for the text. |
| **bg**       | the background color for the text. |

## Return Value

Returns a new 32-bit, ARGB surface, or NULL if there was an error.

## Remarks

This function will allocate a new 32-bit, ARGB surface, and render
alpha-blended text using FreeType's LCD subpixel rendering. This function
returns the new surface, or NULL if there was an error.

The glyph is rendered without any padding or centering in the X direction,
and aligned normally in the Y direction.

Note that this version of the function takes a 16-bit character code, which
covers the Basic Multilingual Plane, but is insufficient to cover the
entire set of possible Unicode values, including emoji glyphs. You should
use [TTF_RenderGlyph32_LCD](TTF_RenderGlyph32_LCD)() instead, which offers
the same functionality but takes a 32-bit codepoint instead.

This function only exists for consistency with the existing API at the time
of its addition.

You can render at other quality levels with
[TTF_RenderGlyph_Solid](TTF_RenderGlyph_Solid),
[TTF_RenderGlyph_Shaded](TTF_RenderGlyph_Shaded), and
[TTF_RenderGlyph_Blended](TTF_RenderGlyph_Blended).

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_RenderGlyph32_LCD](TTF_RenderGlyph32_LCD)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

