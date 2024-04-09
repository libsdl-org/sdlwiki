###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_RenderText_Blended

Render Latin1 text at high quality to a new ARGB surface.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
SDL_Surface * TTF_RenderText_Blended(TTF_Font *font,
                const char *text, SDL_Color fg);

```

## Function Parameters

|              |                                     |
| ------------ | ----------------------------------- |
| **font**     | the font to render with.            |
| **text**     | text to render, in Latin1 encoding. |
| **fg**       | the foreground color for the text.  |

## Return Value

Returns a new 32-bit, ARGB surface, or NULL if there was an error.

## Remarks

This function will allocate a new 32-bit, ARGB surface, using alpha
blending to dither the font with the given color. This function returns the
new surface, or NULL if there was an error.

This will not word-wrap the string; you'll get a surface with a single line
of text, as long as the string requires. You can use
[TTF_RenderText_Blended_Wrapped](TTF_RenderText_Blended_Wrapped)() instead
if you need to wrap the output to multiple lines.

This will not wrap on newline characters.

You almost certainly want
[TTF_RenderUTF8_Blended](TTF_RenderUTF8_Blended)() unless you're sure you
have a 1-byte Latin1 encoding. US ASCII characters will work with either
function, but most other Unicode characters packed into a `const char *`
will need UTF-8.

You can render at other quality levels with
[TTF_RenderText_Solid](TTF_RenderText_Solid),
[TTF_RenderText_Blended](TTF_RenderText_Blended), and
[TTF_RenderText_LCD](TTF_RenderText_LCD).

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

* [TTF_RenderUTF8_Shaded](TTF_RenderUTF8_Shaded)
* [TTF_RenderUNICODE_Shaded](TTF_RenderUNICODE_Shaded)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

