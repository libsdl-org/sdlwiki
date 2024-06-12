###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderUTF8_Shaded

Render UTF-8 text at high quality to a new 8-bit surface.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
SDL_Surface * TTF_RenderUTF8_Shaded(TTF_Font *font,
                const char *text, SDL_Color fg, SDL_Color bg);
```

## Function Parameters

|                        |          |                                    |
| ---------------------- | -------- | ---------------------------------- |
| [TTF_Font](TTF_Font) * | **font** | the font to render with.           |
| const char *           | **text** | text to render, in UTF-8 encoding. |
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

This will not word-wrap the string; you'll get a surface with a single line
of text, as long as the string requires. You can use
[TTF_RenderUTF8_Shaded_Wrapped](TTF_RenderUTF8_Shaded_Wrapped)() instead if
you need to wrap the output to multiple lines.

This will not wrap on newline characters.

You can render at other quality levels with
[TTF_RenderUTF8_Solid](TTF_RenderUTF8_Solid),
[TTF_RenderUTF8_Blended](TTF_RenderUTF8_Blended), and
[TTF_RenderUTF8_LCD](TTF_RenderUTF8_LCD).

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_RenderUNICODE_Shaded](TTF_RenderUNICODE_Shaded)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

