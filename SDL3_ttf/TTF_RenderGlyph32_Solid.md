###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderGlyph32_Solid

Render a single 32-bit glyph at fast quality to a new 8-bit surface.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
SDL_Surface * TTF_RenderGlyph32_Solid(TTF_Font *font,
                Uint32 ch, SDL_Color fg);

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

This is the same as [TTF_RenderGlyph_Solid](TTF_RenderGlyph_Solid)(), but
takes a 32-bit character instead of 16-bit, and thus can render a larger
range. If you are sure you'll have an SDL_ttf that's version 2.0.18 or
newer, there's no reason not to use this function exclusively.

You can render at other quality levels with
[TTF_RenderGlyph32_Shaded](TTF_RenderGlyph32_Shaded),
[TTF_RenderGlyph32_Blended](TTF_RenderGlyph32_Blended), and
[TTF_RenderGlyph32_LCD](TTF_RenderGlyph32_LCD).

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

* [TTF_RenderGlyph32_Shaded](TTF_RenderGlyph32_Shaded)
* [TTF_RenderGlyph32_Blended](TTF_RenderGlyph32_Blended)
* [TTF_RenderGlyph32_LCD](TTF_RenderGlyph32_LCD)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

