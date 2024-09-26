###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GlyphIsProvided

Check whether a glyph is provided by the font for a 32-bit codepoint.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GlyphIsProvided(TTF_Font *font, Uint32 ch);
```

## Function Parameters

|                        |          |                              |
| ---------------------- | -------- | ---------------------------- |
| [TTF_Font](TTF_Font) * | **font** | the font to query.           |
| Uint32                 | **ch**   | the character code to check. |

## Return Value

(bool) Returns true if font provides a glyph for this character, false if
not.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

