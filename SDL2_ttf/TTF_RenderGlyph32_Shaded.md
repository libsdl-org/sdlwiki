###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderGlyph32_Shaded

Render a single 32-bit glyph at high quality to a new 8-bit surface.

## Header File

Defined in [<SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/SDL2/include/SDL_ttf.h)

## Syntax

```c
SDL_Surface * TTF_RenderGlyph32_Shaded(TTF_Font *font,
                Uint32 ch, SDL_Color fg, SDL_Color bg);
```

## Function Parameters

|                        |          |                                    |
| ---------------------- | -------- | ---------------------------------- |
| [TTF_Font](TTF_Font) * | **font** | the font to render with.           |
| Uint32                 | **ch**   | the character to render.           |
| SDL_Color              | **fg**   | the foreground color for the text. |

## Return Value

(SDL_Surface *) Returns a new 8-bit, palettized surface, or NULL if there
was an error.

## Remarks

This function will allocate a new 8-bit, palettized surface. The surface's
0 pixel will be the specified background color, while other pixels have
varying degrees of the foreground color. This function returns the new
surface, or NULL if there was an error.

The glyph is rendered without any padding or centering in the X direction,
and aligned normally in the Y direction.

This is the same as [TTF_RenderGlyph_Shaded](TTF_RenderGlyph_Shaded)(), but
takes a 32-bit character instead of 16-bit, and thus can render a larger
range. If you are sure you'll have an SDL_ttf that's version 2.0.18 or
newer, there's no reason not to use this function exclusively.

You can render at other quality levels with
[TTF_RenderGlyph32_Solid](TTF_RenderGlyph32_Solid),
[TTF_RenderGlyph32_Blended](TTF_RenderGlyph32_Blended), and
[TTF_RenderGlyph32_LCD](TTF_RenderGlyph32_LCD).

## Version

This function is available since SDL_ttf 2.0.18.

## See Also

- [TTF_RenderGlyph32_Solid](TTF_RenderGlyph32_Solid)
- [TTF_RenderGlyph32_Blended](TTF_RenderGlyph32_Blended)
- [TTF_RenderGlyph32_LCD](TTF_RenderGlyph32_LCD)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

