###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderGlyph32_LCD

Render a single 32-bit glyph at LCD subpixel quality to a new ARGB surface.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
SDL_Surface * TTF_RenderGlyph32_LCD(TTF_Font *font,
                Uint32 ch, SDL_Color fg, SDL_Color bg);

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

This is the same as [TTF_RenderGlyph_LCD](TTF_RenderGlyph_LCD)(), but takes
a 32-bit character instead of 16-bit, and thus can render a larger range.
Between the two, you should always use this function.

You can render at other quality levels with
[TTF_RenderGlyph32_Solid](TTF_RenderGlyph32_Solid),
[TTF_RenderGlyph32_Shaded](TTF_RenderGlyph32_Shaded), and
[TTF_RenderGlyph32_Blended](TTF_RenderGlyph32_Blended).

## Version

This function is available since SDL_ttf 2.20.0.

## See Also

- [TTF_RenderGlyph32_Solid](TTF_RenderGlyph32_Solid)
- [TTF_RenderGlyph32_Shaded](TTF_RenderGlyph32_Shaded)
- [TTF_RenderGlyph32_Blended](TTF_RenderGlyph32_Blended)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

