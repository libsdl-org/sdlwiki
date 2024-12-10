###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_FontHasGlyph

Check whether a glyph is provided by the font for a UNICODE codepoint.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_FontHasGlyph(TTF_Font *font, Uint32 ch);
```

## Function Parameters

|                        |          |                         |
| ---------------------- | -------- | ----------------------- |
| [TTF_Font](TTF_Font) * | **font** | the font to query.      |
| Uint32                 | **ch**   | the codepoint to check. |

## Return Value

(bool) Returns true if font provides a glyph for this character, false if
not.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

