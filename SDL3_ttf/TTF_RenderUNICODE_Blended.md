###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderUNICODE_Blended

Render UCS-2 text at high quality to a new ARGB surface.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
SDL_Surface * TTF_RenderUNICODE_Blended(TTF_Font *font,
                const Uint16 *text, SDL_Color fg);
```

## Function Parameters

|                        |          |                                    |
| ---------------------- | -------- | ---------------------------------- |
| [TTF_Font](TTF_Font) * | **font** | the font to render with.           |
| const Uint16 *         | **text** | text to render, in UCS-2 encoding. |
| SDL_Color              | **fg**   | the foreground color for the text. |

## Return Value

(SDL_Surface *) Returns a new 32-bit, ARGB surface, or NULL if there was an
error.

## Remarks

This function will allocate a new 32-bit, ARGB surface, using alpha
blending to dither the font with the given color. This function returns the
new surface, or NULL if there was an error.

This will not word-wrap the string; you'll get a surface with a single line
of text, as long as the string requires. You can use
[TTF_RenderUNICODE_Blended_Wrapped](TTF_RenderUNICODE_Blended_Wrapped)()
instead if you need to wrap the output to multiple lines.

This will not wrap on newline characters.

Please note that this function is named "Unicode" but currently expects
UCS-2 encoding (16 bits per codepoint). This does not give you access to
large Unicode values, such as emoji glyphs. These codepoints are accessible
through the UTF-8 version of this function.

You can render at other quality levels with
[TTF_RenderUNICODE_Solid](TTF_RenderUNICODE_Solid),
[TTF_RenderUNICODE_Shaded](TTF_RenderUNICODE_Shaded), and
[TTF_RenderUNICODE_LCD](TTF_RenderUNICODE_LCD).

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_RenderUTF8_Blended](TTF_RenderUTF8_Blended)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

