###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GlyphIsProvided

Check whether a glyph is provided by the font for a 16-bit codepoint.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
int TTF_GlyphIsProvided(TTF_Font *font, Uint16 ch);

```

## Function Parameters

|              |                              |
| ------------ | ---------------------------- |
| **font**     | the font to query.           |
| **ch**       | the character code to check. |

## Return Value

Returns non-zero if font provides a glyph for this character, zero if not.

## Remarks

Note that this version of the function takes a 16-bit character code, which
covers the Basic Multilingual Plane, but is insufficient to cover the
entire set of possible Unicode values, including emoji glyphs. You should
use [TTF_GlyphIsProvided32](TTF_GlyphIsProvided32)() instead, which offers
the same functionality but takes a 32-bit codepoint instead.

The only reason to use this function is that it was available since the
beginning of time, more or less.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

* [TTF_GlyphIsProvided32](TTF_GlyphIsProvided32)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

