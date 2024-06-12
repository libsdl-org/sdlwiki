###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderGlyph_Shaded

Render a single 16-bit glyph at high quality to a new 8-bit surface.

## Header File

Defined in [<SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/SDL2/include/SDL_ttf.h)

## Syntax

```c
SDL_Surface * TTF_RenderGlyph_Shaded(TTF_Font *font,
                Uint16 ch, SDL_Color fg, SDL_Color bg);
```

## Function Parameters

|                        |          |                                    |
| ---------------------- | -------- | ---------------------------------- |
| [TTF_Font](TTF_Font) * | **font** | the font to render with.           |
| Uint16                 | **ch**   | the character to render.           |
| SDL_Color              | **fg**   | the foreground color for the text. |
| SDL_Color              | **bg**   | the background color for the text. |

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

Note that this version of the function takes a 16-bit character code, which
covers the Basic Multilingual Plane, but is insufficient to cover the
entire set of possible Unicode values, including emoji glyphs. You should
use [TTF_RenderGlyph32_Shaded](TTF_RenderGlyph32_Shaded)() instead, which
offers the same functionality but takes a 32-bit codepoint instead.

The only reason to use this function is that it was available since the
beginning of time, more or less.

You can render at other quality levels with
[TTF_RenderGlyph_Solid](TTF_RenderGlyph_Solid),
[TTF_RenderGlyph_Blended](TTF_RenderGlyph_Blended), and
[TTF_RenderGlyph_LCD](TTF_RenderGlyph_LCD).

## Version

This function is available since SDL_ttf 2.0.12.

## See Also

- [TTF_RenderGlyph32_Shaded](TTF_RenderGlyph32_Shaded)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

