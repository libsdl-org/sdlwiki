###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GlyphIsProvided32

Check whether a glyph is provided by the font for a 32-bit codepoint.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
int TTF_GlyphIsProvided32(TTF_Font *font, Uint32 ch);
```

## Function Parameters

|                        |          |                              |
| ---------------------- | -------- | ---------------------------- |
| [TTF_Font](TTF_Font) * | **font** | the font to query.           |
| Uint32                 | **ch**   | the character code to check. |

## Return Value

(int) Returns non-zero if font provides a glyph for this character, zero if
not.

## Remarks

This is the same as [TTF_GlyphIsProvided](TTF_GlyphIsProvided)(), but takes
a 32-bit character instead of 16-bit, and thus can query a larger range. If
you are sure you'll have an SDL_ttf that's version 2.0.18 or newer, there's
no reason not to use this function exclusively.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

