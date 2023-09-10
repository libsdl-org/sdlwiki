###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderGlyph32_Blended

Render a single 32-bit glyph at high quality to a new ARGB surface.

## Syntax

```c
SDL_Surface * TTF_RenderGlyph32_Blended(TTF_Font *font,
                Uint32 ch, SDL_Color fg);

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

This is the same as [TTF_RenderGlyph_Blended](TTF_RenderGlyph_Blended)(),
but takes a 32-bit character instead of 16-bit, and thus can render a
larger range. If you are sure you'll have an SDL_ttf that's version 2.0.18
or newer, there's no reason not to use this function exclusively.

You can render at other quality levels with
[TTF_RenderGlyph32_Solid](TTF_RenderGlyph32_Solid),
[TTF_RenderGlyph32_Shaded](TTF_RenderGlyph32_Shaded), and
[TTF_RenderGlyph32_LCD](TTF_RenderGlyph32_LCD).

## Version

This function is available since SDL_ttf 3.0.0.

## Related Functions

* [TTF_RenderGlyph32_Solid](TTF_RenderGlyph32_Solid)
* [TTF_RenderGlyph32_Shaded](TTF_RenderGlyph32_Shaded)
* [TTF_RenderGlyph32_LCD](TTF_RenderGlyph32_LCD)

----
[CategoryAPI](CategoryAPI)

