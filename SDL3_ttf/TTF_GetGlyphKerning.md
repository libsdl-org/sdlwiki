###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetGlyphKerning

Query the kerning size between the glyphs of two UNICODE codepoints.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetGlyphKerning(TTF_Font *font, Uint32 previous_ch, Uint32 ch, int *kerning);
```

## Function Parameters

|                        |                 |                                                                                           |
| ---------------------- | --------------- | ----------------------------------------------------------------------------------------- |
| [TTF_Font](TTF_Font) * | **font**        | the font to query.                                                                        |
| Uint32                 | **previous_ch** | the previous codepoint.                                                                   |
| Uint32                 | **ch**          | the current codepoint.                                                                    |
| int *                  | **kerning**     | a pointer filled in with the kerning size between the two glyphs, in pixels, may be NULL. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

