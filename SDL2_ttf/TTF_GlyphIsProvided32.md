###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GlyphIsProvided32

Check whether a glyph is provided by the font for a 32-bit codepoint.

## Syntax

```c
int TTF_GlyphIsProvided32(TTF_Font *font, Uint32 ch);

```

## Function Parameters

|              |                              |
| ------------ | ---------------------------- |
| **font**     | the font to query.           |
| **ch**       | the character code to check. |

## Return Value

Returns non-zero if font provides a glyph for this character, zero if not.

## Remarks

This is the same as [TTF_GlyphIsProvided](TTF_GlyphIsProvided)(), but takes
a 32-bit character instead of 16-bit, and thus can query a larger range. If
you are sure you'll have an SDL_ttf that's version 2.0.18 or newer, there's
no reason not to use this function exclusively.

## Version

This function is available since SDL_ttf 2.0.18.

----
[CategoryAPI](CategoryAPI)

